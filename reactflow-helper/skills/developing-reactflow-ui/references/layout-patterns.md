# React Flow 레이아웃 패턴

## 자동 레이아웃 옵션

| 라이브러리 | 특징 | 설치 |
|------------|------|------|
| Dagre | 계층적 레이아웃, 간단함 | `npm install @dagrejs/dagre` |
| ELK | 복잡한 레이아웃, 다양한 옵션 | `npm install elkjs` |
| D3 Force | 물리 기반, 동적 | `npm install d3-force` |

## Dagre 레이아웃 구현

```typescript
import dagre from '@dagrejs/dagre';
import { Node, Edge, Position } from '@xyflow/react';

const dagreGraph = new dagre.graphlib.Graph();
dagreGraph.setDefaultEdgeLabel(() => ({}));

const nodeWidth = 172;
const nodeHeight = 36;

export function getLayoutedElements(
  nodes: Node[],
  edges: Edge[],
  direction = 'TB' // TB, BT, LR, RL
) {
  const isHorizontal = direction === 'LR' || direction === 'RL';
  dagreGraph.setGraph({ rankdir: direction });

  nodes.forEach((node) => {
    dagreGraph.setNode(node.id, { width: nodeWidth, height: nodeHeight });
  });

  edges.forEach((edge) => {
    dagreGraph.setEdge(edge.source, edge.target);
  });

  dagre.layout(dagreGraph);

  const newNodes = nodes.map((node) => {
    const nodeWithPosition = dagreGraph.node(node.id);
    const newNode = {
      ...node,
      targetPosition: isHorizontal ? Position.Left : Position.Top,
      sourcePosition: isHorizontal ? Position.Right : Position.Bottom,
      position: {
        x: nodeWithPosition.x - nodeWidth / 2,
        y: nodeWithPosition.y - nodeHeight / 2,
      },
    };
    return newNode;
  });

  return { nodes: newNodes, edges };
}
```

## Dagre 사용 예시

```typescript
import { useCallback } from 'react';
import { ReactFlow, useNodesState, useEdgesState, Panel } from '@xyflow/react';
import { getLayoutedElements } from './layout';

function Flow() {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onLayout = useCallback(
    (direction: string) => {
      const { nodes: layoutedNodes, edges: layoutedEdges } =
        getLayoutedElements(nodes, edges, direction);

      setNodes([...layoutedNodes]);
      setEdges([...layoutedEdges]);
    },
    [nodes, edges, setNodes, setEdges]
  );

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      fitView
    >
      <Panel position="top-right">
        <button onClick={() => onLayout('TB')}>세로 레이아웃</button>
        <button onClick={() => onLayout('LR')}>가로 레이아웃</button>
      </Panel>
    </ReactFlow>
  );
}
```

## ELK 레이아웃 구현

```typescript
import ELK from 'elkjs/lib/elk.bundled.js';
import { Node, Edge } from '@xyflow/react';

const elk = new ELK();

const elkOptions = {
  'elk.algorithm': 'layered',
  'elk.layered.spacing.nodeNodeBetweenLayers': '100',
  'elk.spacing.nodeNode': '80',
};

export async function getLayoutedElements(
  nodes: Node[],
  edges: Edge[],
  options = {}
): Promise<{ nodes: Node[]; edges: Edge[] }> {
  const graph = {
    id: 'root',
    layoutOptions: { ...elkOptions, ...options },
    children: nodes.map((node) => ({
      ...node,
      width: 150,
      height: 50,
    })),
    edges: edges.map((edge) => ({
      ...edge,
      sources: [edge.source],
      targets: [edge.target],
    })),
  };

  const layoutedGraph = await elk.layout(graph);

  return {
    nodes: nodes.map((node) => {
      const layoutedNode = layoutedGraph.children?.find((n) => n.id === node.id);
      return {
        ...node,
        position: {
          x: layoutedNode?.x ?? 0,
          y: layoutedNode?.y ?? 0,
        },
      };
    }),
    edges,
  };
}
```

## D3 Force 레이아웃 (동적)

```typescript
import {
  forceSimulation,
  forceLink,
  forceManyBody,
  forceCenter,
  forceCollide
} from 'd3-force';
import { Node, Edge } from '@xyflow/react';

export function useForceLayout(nodes: Node[], edges: Edge[]) {
  const simulation = forceSimulation(nodes as any)
    .force('link', forceLink(edges as any)
      .id((d: any) => d.id)
      .distance(100)
    )
    .force('charge', forceManyBody().strength(-300))
    .force('center', forceCenter(400, 300))
    .force('collide', forceCollide().radius(50));

  // 시뮬레이션이 안정화될 때까지 실행
  simulation.tick(300);

  return {
    nodes: nodes.map((node: any) => ({
      ...node,
      position: { x: node.x, y: node.y },
    })),
    edges,
  };
}
```

## 트리 레이아웃

```typescript
interface TreeNode extends Node {
  children?: string[];
}

export function treeLayout(
  nodes: TreeNode[],
  edges: Edge[],
  rootId: string,
  spacing = { x: 200, y: 100 }
): Node[] {
  const nodeMap = new Map(nodes.map(n => [n.id, n]));
  const visited = new Set<string>();

  function layoutNode(
    nodeId: string,
    x: number,
    y: number,
    level: number
  ): Node[] {
    if (visited.has(nodeId)) return [];
    visited.add(nodeId);

    const node = nodeMap.get(nodeId);
    if (!node) return [];

    const result: Node[] = [{
      ...node,
      position: { x, y },
    }];

    const children = edges
      .filter(e => e.source === nodeId)
      .map(e => e.target);

    const childWidth = spacing.x;
    const startX = x - ((children.length - 1) * childWidth) / 2;

    children.forEach((childId, index) => {
      result.push(...layoutNode(
        childId,
        startX + index * childWidth,
        y + spacing.y,
        level + 1
      ));
    });

    return result;
  }

  return layoutNode(rootId, 400, 50, 0);
}
```

## 레이아웃 트랜지션 애니메이션

```typescript
import { useCallback } from 'react';
import { Node, useReactFlow } from '@xyflow/react';

export function useLayoutAnimation() {
  const { setNodes, fitView } = useReactFlow();

  const animateToLayout = useCallback((targetNodes: Node[]) => {
    const duration = 300;
    const startTime = Date.now();

    const animate = () => {
      const elapsed = Date.now() - startTime;
      const progress = Math.min(elapsed / duration, 1);
      // ease-out 함수
      const eased = 1 - Math.pow(1 - progress, 3);

      setNodes((nodes) =>
        nodes.map((node) => {
          const target = targetNodes.find((n) => n.id === node.id);
          if (!target) return node;

          return {
            ...node,
            position: {
              x: node.position.x + (target.position.x - node.position.x) * eased,
              y: node.position.y + (target.position.y - node.position.y) * eased,
            },
          };
        })
      );

      if (progress < 1) {
        requestAnimationFrame(animate);
      } else {
        fitView({ duration: 200 });
      }
    };

    requestAnimationFrame(animate);
  }, [setNodes, fitView]);

  return { animateToLayout };
}
```

## 레이아웃 방향 옵션

| 방향 | 코드 | 설명 |
|------|------|------|
| 위에서 아래 | `TB` | Top to Bottom |
| 아래에서 위 | `BT` | Bottom to Top |
| 왼쪽에서 오른쪽 | `LR` | Left to Right |
| 오른쪽에서 왼쪽 | `RL` | Right to Left |
