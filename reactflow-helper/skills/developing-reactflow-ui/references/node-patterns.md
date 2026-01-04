# React Flow 노드 패턴

## 기본 노드 생성

```typescript
import { Node } from '@xyflow/react';

const nodes: Node[] = [
  {
    id: '1',
    type: 'default', // 'input' | 'output' | 'default' | custom
    position: { x: 0, y: 0 },
    data: { label: 'Node 1' },
  },
];
```

## 기본 노드 타입

| 타입 | 설명 | 핸들 |
|------|------|------|
| `default` | 기본 노드 | 상단 target, 하단 source |
| `input` | 입력 노드 | 하단 source만 |
| `output` | 출력 노드 | 상단 target만 |

## 커스텀 노드 기본 템플릿

```typescript
import { memo } from 'react';
import { Handle, Position, NodeProps } from '@xyflow/react';

export type CustomNodeData = {
  label: string;
  // 추가 데이터 타입
};

function CustomNode({ data, isConnectable }: NodeProps<CustomNodeData>) {
  return (
    <div className="custom-node">
      <Handle
        type="target"
        position={Position.Top}
        isConnectable={isConnectable}
      />
      <div className="node-content">
        {data.label}
      </div>
      <Handle
        type="source"
        position={Position.Bottom}
        isConnectable={isConnectable}
      />
    </div>
  );
}

export default memo(CustomNode);
```

## 노드 타입 등록

```typescript
import { ReactFlow } from '@xyflow/react';
import { useMemo } from 'react';

const nodeTypes = {
  custom: CustomNode,
  // 추가 커스텀 노드들
};

function Flow() {
  // useMemo로 감싸서 리렌더링 방지 (중요!)
  const memoizedNodeTypes = useMemo(() => nodeTypes, []);

  return (
    <ReactFlow
      nodeTypes={memoizedNodeTypes}
      nodes={nodes}
      edges={edges}
    />
  );
}
```

## 리사이저블 노드

```typescript
import { memo } from 'react';
import { Handle, Position, NodeProps, NodeResizer } from '@xyflow/react';

function ResizableNode({ data, selected }: NodeProps) {
  return (
    <>
      <NodeResizer
        minWidth={100}
        minHeight={50}
        isVisible={selected}
      />
      <Handle type="target" position={Position.Top} />
      <div className="node-content">{data.label}</div>
      <Handle type="source" position={Position.Bottom} />
    </>
  );
}

export default memo(ResizableNode);
```

## 툴바가 있는 노드

```typescript
import { memo } from 'react';
import { Handle, Position, NodeProps, NodeToolbar } from '@xyflow/react';

function ToolbarNode({ data, selected }: NodeProps) {
  return (
    <>
      <NodeToolbar isVisible={selected} position={Position.Top}>
        <button onClick={() => console.log('edit')}>Edit</button>
        <button onClick={() => console.log('delete')}>Delete</button>
      </NodeToolbar>
      <Handle type="target" position={Position.Top} />
      <div className="node-content">{data.label}</div>
      <Handle type="source" position={Position.Bottom} />
    </>
  );
}

export default memo(ToolbarNode);
```

## 다중 핸들 노드

```typescript
import { memo } from 'react';
import { Handle, Position, NodeProps } from '@xyflow/react';

function MultiHandleNode({ data, isConnectable }: NodeProps) {
  return (
    <div className="multi-handle-node">
      <Handle
        type="target"
        position={Position.Top}
        id="t1"
        isConnectable={isConnectable}
      />
      <Handle
        type="target"
        position={Position.Left}
        id="t2"
        style={{ top: '50%' }}
        isConnectable={isConnectable}
      />
      <div className="node-content">{data.label}</div>
      <Handle
        type="source"
        position={Position.Right}
        id="s1"
        style={{ top: '50%' }}
        isConnectable={isConnectable}
      />
      <Handle
        type="source"
        position={Position.Bottom}
        id="s2"
        isConnectable={isConnectable}
      />
    </div>
  );
}

export default memo(MultiHandleNode);
```

## 노드 스타일링 기본 CSS

```css
.custom-node {
  padding: 10px 20px;
  border-radius: 8px;
  background: white;
  border: 1px solid #ddd;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.custom-node.selected {
  border-color: #1a192b;
  box-shadow: 0 0 0 2px rgba(26, 25, 43, 0.2);
}

.react-flow__handle {
  width: 10px;
  height: 10px;
  background: #555;
  border: 2px solid white;
}
```

## 성능 최적화 팁

1. **memo() 사용**: 모든 커스텀 노드는 `memo()`로 감싸기
2. **nodeTypes는 useMemo**: 렌더링마다 새 객체 생성 방지
3. **이벤트 핸들러 useCallback**: 노드 내 핸들러는 useCallback 사용
4. **복잡한 노드 분리**: 서브 컴포넌트로 분리하여 부분 리렌더링
