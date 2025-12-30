# React Flow TypeScript 타입

## 핵심 타입

### Node 타입

```typescript
import { Node, NodeProps } from '@xyflow/react';

// 기본 Node 타입
interface Node<T = any, U extends string = string> {
  id: string;
  position: XYPosition;
  data: T;
  type?: U;
  style?: CSSProperties;
  className?: string;
  sourcePosition?: Position;
  targetPosition?: Position;
  hidden?: boolean;
  selected?: boolean;
  dragging?: boolean;
  draggable?: boolean;
  selectable?: boolean;
  connectable?: boolean;
  deletable?: boolean;
  dragHandle?: string;
  width?: number;
  height?: number;
  parentId?: string;
  zIndex?: number;
  extent?: 'parent' | CoordinateExtent;
  expandParent?: boolean;
  ariaLabel?: string;
  focusable?: boolean;
  resizing?: boolean;
  origin?: NodeOrigin;
  measured?: {
    width?: number;
    height?: number;
  };
}
```

### Edge 타입

```typescript
import { Edge, EdgeProps } from '@xyflow/react';

interface Edge<T = any> {
  id: string;
  source: string;
  target: string;
  sourceHandle?: string | null;
  targetHandle?: string | null;
  type?: string;
  data?: T;
  style?: CSSProperties;
  className?: string;
  animated?: boolean;
  hidden?: boolean;
  deletable?: boolean;
  selectable?: boolean;
  selected?: boolean;
  focusable?: boolean;
  label?: string | ReactNode;
  labelStyle?: CSSProperties;
  labelShowBg?: boolean;
  labelBgStyle?: CSSProperties;
  labelBgPadding?: [number, number];
  labelBgBorderRadius?: number;
  markerStart?: EdgeMarker;
  markerEnd?: EdgeMarker;
  interactionWidth?: number;
  zIndex?: number;
  ariaLabel?: string;
}
```

### Position 열거형

```typescript
import { Position } from '@xyflow/react';

enum Position {
  Left = 'left',
  Top = 'top',
  Right = 'right',
  Bottom = 'bottom',
}
```

## 커스텀 노드 Props 타입

```typescript
import { NodeProps } from '@xyflow/react';

// 커스텀 데이터 타입 정의
type MyNodeData = {
  label: string;
  value: number;
  status: 'active' | 'inactive';
};

// 커스텀 노드 컴포넌트
function MyNode({
  data,           // MyNodeData
  id,             // string
  selected,       // boolean
  isConnectable,  // boolean
  xPos,           // number
  yPos,           // number
  zIndex,         // number
  dragging,       // boolean
  type,           // string
  sourcePosition, // Position
  targetPosition, // Position
}: NodeProps<MyNodeData>) {
  return (
    <div>
      <span>{data.label}</span>
      <span>{data.value}</span>
    </div>
  );
}
```

## 커스텀 엣지 Props 타입

```typescript
import { EdgeProps } from '@xyflow/react';

type MyEdgeData = {
  label: string;
  weight: number;
};

function MyEdge({
  id,             // string
  source,         // string
  target,         // string
  sourceX,        // number
  sourceY,        // number
  targetX,        // number
  targetY,        // number
  sourcePosition, // Position
  targetPosition, // Position
  data,           // MyEdgeData
  markerEnd,      // string
  style,          // CSSProperties
  selected,       // boolean
  animated,       // boolean
  interactionWidth, // number
}: EdgeProps<MyEdgeData>) {
  // ...
}
```

## useReactFlow 타입

```typescript
import { useReactFlow } from '@xyflow/react';

// 반환 타입
interface ReactFlowInstance<NodeType = any, EdgeType = any> {
  // 상태 접근
  getNodes: () => Node<NodeType>[];
  getEdges: () => Edge<EdgeType>[];
  getNode: (id: string) => Node<NodeType> | undefined;
  getEdge: (id: string) => Edge<EdgeType> | undefined;

  // 상태 수정
  setNodes: (nodes: Node<NodeType>[] | ((nodes: Node<NodeType>[]) => Node<NodeType>[])) => void;
  setEdges: (edges: Edge<EdgeType>[] | ((edges: Edge<EdgeType>[]) => Edge<EdgeType>[])) => void;
  addNodes: (nodes: Node<NodeType> | Node<NodeType>[]) => void;
  addEdges: (edges: Edge<EdgeType> | Edge<EdgeType>[]) => void;

  // 뷰포트
  setViewport: (viewport: Viewport, options?: ViewportHelperFunctionOptions) => void;
  getViewport: () => Viewport;
  fitView: (options?: FitViewOptions) => boolean;
  zoomIn: (options?: ViewportHelperFunctionOptions) => void;
  zoomOut: (options?: ViewportHelperFunctionOptions) => void;
  zoomTo: (zoomLevel: number, options?: ViewportHelperFunctionOptions) => void;

  // 좌표 변환
  screenToFlowPosition: (position: XYPosition) => XYPosition;
  flowToScreenPosition: (position: XYPosition) => XYPosition;

  // 연결
  getIntersectingNodes: (node: Node | Rect, partially?: boolean, nodes?: Node[]) => Node[];
  isNodeIntersecting: (node: Node | Rect, area: Rect, partially?: boolean) => boolean;

  // 기타
  updateNode: (id: string, nodeUpdate: Partial<Node<NodeType>> | ((node: Node<NodeType>) => Partial<Node<NodeType>>)) => void;
  updateNodeData: (id: string, dataUpdate: Partial<NodeType> | ((data: NodeType) => Partial<NodeType>)) => void;
  deleteElements: (elements: { nodes?: Node[]; edges?: Edge[] }) => void;
  toObject: () => ReactFlowJsonObject<NodeType, EdgeType>;
}
```

## 상태 훅 타입

```typescript
import {
  useNodesState,
  useEdgesState,
  OnNodesChange,
  OnEdgesChange,
  NodeChange,
  EdgeChange
} from '@xyflow/react';

// useNodesState
const [nodes, setNodes, onNodesChange] = useNodesState<MyNodeData>(initialNodes);
// nodes: Node<MyNodeData>[]
// setNodes: Dispatch<SetStateAction<Node<MyNodeData>[]>>
// onNodesChange: OnNodesChange

// useEdgesState
const [edges, setEdges, onEdgesChange] = useEdgesState<MyEdgeData>(initialEdges);
// edges: Edge<MyEdgeData>[]
// setEdges: Dispatch<SetStateAction<Edge<MyEdgeData>[]>>
// onEdgesChange: OnEdgesChange
```

## 이벤트 핸들러 타입

```typescript
import {
  OnConnect,
  OnConnectStart,
  OnConnectEnd,
  OnSelectionChange,
  OnNodesChange,
  OnEdgesChange,
  NodeMouseHandler,
  EdgeMouseHandler,
} from '@xyflow/react';

// 연결 이벤트
const onConnect: OnConnect = (connection) => {
  // connection: Connection
};

const onConnectStart: OnConnectStart = (event, params) => {
  // event: MouseEvent | TouchEvent
  // params: { nodeId: string | null; handleId: string | null; handleType: HandleType }
};

// 선택 이벤트
const onSelectionChange: OnSelectionChange = ({ nodes, edges }) => {
  // nodes: Node[]
  // edges: Edge[]
};

// 노드 마우스 이벤트
const onNodeClick: NodeMouseHandler = (event, node) => {
  // event: React.MouseEvent
  // node: Node
};

const onNodeDragStop: NodeMouseHandler = (event, node) => {
  // ...
};

// 엣지 마우스 이벤트
const onEdgeClick: EdgeMouseHandler = (event, edge) => {
  // event: React.MouseEvent
  // edge: Edge
};
```

## 유틸리티 타입

```typescript
import {
  XYPosition,
  Rect,
  Viewport,
  Connection,
  HandleType,
  MarkerType,
  CoordinateExtent,
} from '@xyflow/react';

interface XYPosition {
  x: number;
  y: number;
}

interface Rect extends XYPosition {
  width: number;
  height: number;
}

interface Viewport {
  x: number;
  y: number;
  zoom: number;
}

interface Connection {
  source: string | null;
  target: string | null;
  sourceHandle: string | null;
  targetHandle: string | null;
}

type HandleType = 'source' | 'target';

enum MarkerType {
  Arrow = 'arrow',
  ArrowClosed = 'arrowclosed',
}

type CoordinateExtent = [[number, number], [number, number]];
```

## 제네릭 활용 패턴

```typescript
// 프로젝트 전역 타입 정의
export type AppNodeData = {
  label: string;
  status: 'active' | 'pending' | 'error';
};

export type AppEdgeData = {
  weight: number;
};

export type AppNode = Node<AppNodeData>;
export type AppEdge = Edge<AppEdgeData>;

// 컴포넌트에서 사용
function Flow() {
  const [nodes, setNodes] = useNodesState<AppNodeData>(initialNodes);
  const [edges, setEdges] = useEdgesState<AppEdgeData>(initialEdges);
  const { getNodes } = useReactFlow<AppNodeData, AppEdgeData>();

  // 타입 안전한 접근
  const activeNodes = getNodes().filter(n => n.data.status === 'active');
}
```
