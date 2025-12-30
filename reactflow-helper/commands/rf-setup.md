---
description: React Flow 프로젝트 초기 설정을 도와줍니다. 패키지 설치, 기본 구조 생성을 지원합니다.
---

# React Flow 프로젝트 설정

새 프로젝트에 React Flow를 설정합니다.

## 사용 방법

```
/rf-setup [옵션]
```

## 옵션

- `--typescript` : TypeScript 설정 (기본값)
- `--tailwind` : Tailwind CSS 통합
- `--ui` : @xyflow/react UI 컴포넌트 추가
- `--zustand` : Zustand 상태 관리 설정

## 동작 지침

1. 현재 프로젝트 구조 확인 (package.json 존재 여부)
2. 필요시 최신 설치 가이드 확인:
   - WebFetch: `https://r.jina.ai/https://reactflow.dev/learn`
3. 패키지 설치 안내
4. 기본 파일 구조 생성
5. 초기 코드 템플릿 제공

## 패키지 설치

### 기본 설치

```bash
npm install @xyflow/react
# 또는
pnpm add @xyflow/react
# 또는
yarn add @xyflow/react
```

### Tailwind CSS 통합 (--tailwind)

```bash
npm install @xyflow/react tailwindcss postcss autoprefixer
```

### 상태 관리 (--zustand)

```bash
npm install @xyflow/react zustand
```

## 기본 디렉토리 구조

```
src/
├── components/
│   └── flow/
│       ├── Flow.tsx              # 메인 Flow 컴포넌트
│       ├── nodes/
│       │   ├── index.ts          # nodeTypes 등록
│       │   └── CustomNode.tsx    # 커스텀 노드 예시
│       └── edges/
│           ├── index.ts          # edgeTypes 등록
│           └── CustomEdge.tsx    # 커스텀 엣지 예시
├── hooks/
│   └── useFlowStore.ts           # (Zustand 사용시) 상태 관리
└── types/
    └── flow.ts                   # Flow 관련 타입
```

## 기본 코드 템플릿

### Flow.tsx (메인 컴포넌트)

```typescript
import { useCallback } from 'react';
import {
  ReactFlow,
  addEdge,
  useNodesState,
  useEdgesState,
  Controls,
  Background,
  Connection,
  BackgroundVariant,
} from '@xyflow/react';
import '@xyflow/react/dist/style.css';

import { nodeTypes } from './nodes';
import { edgeTypes } from './edges';

const initialNodes = [
  { id: '1', type: 'default', position: { x: 0, y: 0 }, data: { label: 'Node 1' } },
  { id: '2', type: 'default', position: { x: 200, y: 100 }, data: { label: 'Node 2' } },
];

const initialEdges = [
  { id: 'e1-2', source: '1', target: '2' },
];

export default function Flow() {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onConnect = useCallback(
    (connection: Connection) => setEdges((eds) => addEdge(connection, eds)),
    [setEdges]
  );

  return (
    <div style={{ width: '100%', height: '100vh' }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        nodeTypes={nodeTypes}
        edgeTypes={edgeTypes}
        fitView
      >
        <Controls />
        <Background variant={BackgroundVariant.Dots} gap={12} size={1} />
      </ReactFlow>
    </div>
  );
}
```

### nodes/index.ts

```typescript
import { useMemo } from 'react';
import type { NodeTypes } from '@xyflow/react';
// import CustomNode from './CustomNode';

export const nodeTypes: NodeTypes = {
  // custom: CustomNode,
} satisfies NodeTypes;

// Hook for memoized node types
export function useNodeTypes() {
  return useMemo(() => nodeTypes, []);
}
```

### edges/index.ts

```typescript
import { useMemo } from 'react';
import type { EdgeTypes } from '@xyflow/react';
// import CustomEdge from './CustomEdge';

export const edgeTypes: EdgeTypes = {
  // custom: CustomEdge,
} satisfies EdgeTypes;

// Hook for memoized edge types
export function useEdgeTypes() {
  return useMemo(() => edgeTypes, []);
}
```

### types/flow.ts

```typescript
import type { Node, Edge } from '@xyflow/react';

// 프로젝트 전역 노드 데이터 타입
export type AppNodeData = {
  label: string;
  // 추가 필드 정의
};

// 프로젝트 전역 엣지 데이터 타입
export type AppEdgeData = {
  // 엣지 데이터 필드 정의
};

export type AppNode = Node<AppNodeData>;
export type AppEdge = Edge<AppEdgeData>;
```

### Zustand 스토어 (--zustand)

```typescript
// hooks/useFlowStore.ts
import { create } from 'zustand';
import {
  Node,
  Edge,
  Connection,
  addEdge,
  OnNodesChange,
  OnEdgesChange,
  applyNodeChanges,
  applyEdgeChanges,
} from '@xyflow/react';

type FlowState = {
  nodes: Node[];
  edges: Edge[];
  onNodesChange: OnNodesChange;
  onEdgesChange: OnEdgesChange;
  onConnect: (connection: Connection) => void;
  setNodes: (nodes: Node[]) => void;
  setEdges: (edges: Edge[]) => void;
};

export const useFlowStore = create<FlowState>((set, get) => ({
  nodes: [],
  edges: [],
  onNodesChange: (changes) => {
    set({ nodes: applyNodeChanges(changes, get().nodes) });
  },
  onEdgesChange: (changes) => {
    set({ edges: applyEdgeChanges(changes, get().edges) });
  },
  onConnect: (connection) => {
    set({ edges: addEdge(connection, get().edges) });
  },
  setNodes: (nodes) => set({ nodes }),
  setEdges: (edges) => set({ edges }),
}));
```

## 필수 CSS

```css
/* styles.css 또는 globals.css에 추가 */
@import '@xyflow/react/dist/style.css';
```

## 체크리스트

- [ ] @xyflow/react 패키지 설치
- [ ] CSS import 추가
- [ ] Flow 컴포넌트 생성
- [ ] nodeTypes/edgeTypes 등록 준비
- [ ] (선택) 상태 관리 설정
- [ ] (선택) 커스텀 스타일 추가
