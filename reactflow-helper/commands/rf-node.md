---
description: React Flow 커스텀 노드를 생성합니다. 다양한 템플릿과 옵션을 지원합니다.
---

# React Flow 노드 생성

커스텀 노드 컴포넌트를 생성합니다.

## 사용 방법

```
/rf-node [노드이름] [옵션]
```

## 옵션

- `--handles` : 핸들 위치 지정 (top, bottom, left, right, all)
- `--resizable` : 리사이징 가능 노드
- `--toolbar` : 노드 툴바 포함
- `--multiple-handles` : 다중 핸들 지원

## 동작 지침

1. 노드 이름과 옵션 파싱
2. 필요시 최신 문서 확인:
   - WebFetch: `https://r.jina.ai/https://reactflow.dev/learn/customization/custom-nodes`
3. 노드 컴포넌트 코드 생성
4. TypeScript 타입 정의 생성
5. nodeTypes 등록 방법 안내

## 생성 템플릿

### 기본 노드

```typescript
import { memo } from 'react';
import { Handle, Position, NodeProps } from '@xyflow/react';

export type {NodeName}Data = {
  label: string;
  // 추가 데이터 필드
};

function {NodeName}Node({ data, isConnectable }: NodeProps<{NodeName}Data>) {
  return (
    <div className="{node-name}-node">
      <Handle type="target" position={Position.Top} isConnectable={isConnectable} />
      <div className="node-content">
        {data.label}
      </div>
      <Handle type="source" position={Position.Bottom} isConnectable={isConnectable} />
    </div>
  );
}

export default memo({NodeName}Node);
```

### 리사이저블 노드 (--resizable)

```typescript
import { memo } from 'react';
import { Handle, Position, NodeProps, NodeResizer } from '@xyflow/react';

function {NodeName}Node({ data, selected, isConnectable }: NodeProps<{NodeName}Data>) {
  return (
    <>
      <NodeResizer minWidth={100} minHeight={50} isVisible={selected} />
      <Handle type="target" position={Position.Top} isConnectable={isConnectable} />
      <div className="node-content">{data.label}</div>
      <Handle type="source" position={Position.Bottom} isConnectable={isConnectable} />
    </>
  );
}

export default memo({NodeName}Node);
```

### 툴바 노드 (--toolbar)

```typescript
import { memo } from 'react';
import { Handle, Position, NodeProps, NodeToolbar } from '@xyflow/react';

function {NodeName}Node({ data, selected, isConnectable }: NodeProps<{NodeName}Data>) {
  return (
    <>
      <NodeToolbar isVisible={selected} position={Position.Top}>
        <button onClick={() => console.log('edit')}>Edit</button>
        <button onClick={() => console.log('delete')}>Delete</button>
      </NodeToolbar>
      <Handle type="target" position={Position.Top} isConnectable={isConnectable} />
      <div className="node-content">{data.label}</div>
      <Handle type="source" position={Position.Bottom} isConnectable={isConnectable} />
    </>
  );
}

export default memo({NodeName}Node);
```

## nodeTypes 등록 안내

```typescript
import { ReactFlow } from '@xyflow/react';
import { useMemo } from 'react';
import {NodeName}Node from './nodes/{NodeName}Node';

const nodeTypes = {
  {nodeName}: {NodeName}Node,
};

function Flow() {
  // 반드시 useMemo로 감싸서 리렌더링 방지
  const memoizedNodeTypes = useMemo(() => nodeTypes, []);

  return (
    <ReactFlow
      nodeTypes={memoizedNodeTypes}
      // ... 기타 props
    />
  );
}
```

## 기본 스타일

```css
.{node-name}-node {
  padding: 10px 20px;
  border-radius: 8px;
  background: white;
  border: 1px solid #ddd;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  min-width: 150px;
}

.{node-name}-node.selected {
  border-color: #1a192b;
  box-shadow: 0 0 0 2px rgba(26, 25, 43, 0.2);
}
```
