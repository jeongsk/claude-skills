---
description: React Flow 커스텀 엣지를 생성합니다. 애니메이션, 라벨, 버튼 등을 지원합니다.
---

# React Flow 엣지 생성

커스텀 엣지 컴포넌트를 생성합니다.

## 사용 방법

```
/rf-edge [엣지이름] [옵션]
```

## 옵션

- `--type` : 기본 경로 타입 (bezier, smoothstep, step, straight)
- `--animated` : 애니메이션 엣지
- `--label` : 엣지 라벨 포함
- `--button` : 삭제/액션 버튼 포함

## 동작 지침

1. 엣지 이름과 옵션 파싱
2. 필요시 최신 문서 확인:
   - WebFetch: `https://r.jina.ai/https://reactflow.dev/learn/customization/custom-edges`
3. 엣지 컴포넌트 코드 생성
4. edgeTypes 등록 방법 안내

## 생성 템플릿

### 기본 커스텀 엣지

```typescript
import { memo } from 'react';
import { EdgeProps, getBezierPath } from '@xyflow/react';

export type {EdgeName}Data = {
  label?: string;
};

function {EdgeName}Edge({
  id,
  sourceX,
  sourceY,
  targetX,
  targetY,
  sourcePosition,
  targetPosition,
  style = {},
  markerEnd,
}: EdgeProps<{EdgeName}Data>) {
  const [edgePath] = getBezierPath({
    sourceX,
    sourceY,
    sourcePosition,
    targetX,
    targetY,
    targetPosition,
  });

  return (
    <path
      id={id}
      style={style}
      className="react-flow__edge-path"
      d={edgePath}
      markerEnd={markerEnd}
    />
  );
}

export default memo({EdgeName}Edge);
```

### 라벨이 있는 엣지 (--label)

```typescript
import { memo } from 'react';
import { EdgeProps, getBezierPath, EdgeLabelRenderer } from '@xyflow/react';

function {EdgeName}Edge({
  id,
  sourceX,
  sourceY,
  targetX,
  targetY,
  sourcePosition,
  targetPosition,
  style = {},
  markerEnd,
  data,
}: EdgeProps<{EdgeName}Data>) {
  const [edgePath, labelX, labelY] = getBezierPath({
    sourceX,
    sourceY,
    sourcePosition,
    targetX,
    targetY,
    targetPosition,
  });

  return (
    <>
      <path
        id={id}
        style={style}
        className="react-flow__edge-path"
        d={edgePath}
        markerEnd={markerEnd}
      />
      <EdgeLabelRenderer>
        <div
          style={{
            position: 'absolute',
            transform: `translate(-50%, -50%) translate(${labelX}px,${labelY}px)`,
            background: 'white',
            padding: '4px 8px',
            borderRadius: '4px',
            fontSize: '12px',
            fontWeight: 500,
          }}
          className="nodrag nopan"
        >
          {data?.label}
        </div>
      </EdgeLabelRenderer>
    </>
  );
}

export default memo({EdgeName}Edge);
```

### 버튼이 있는 엣지 (--button)

```typescript
import { memo, useCallback } from 'react';
import { EdgeProps, getBezierPath, EdgeLabelRenderer, useReactFlow } from '@xyflow/react';

function {EdgeName}Edge({
  id,
  sourceX,
  sourceY,
  targetX,
  targetY,
  sourcePosition,
  targetPosition,
  style = {},
  markerEnd,
}: EdgeProps) {
  const { setEdges } = useReactFlow();
  const [edgePath, labelX, labelY] = getBezierPath({
    sourceX,
    sourceY,
    sourcePosition,
    targetX,
    targetY,
    targetPosition,
  });

  const onEdgeClick = useCallback(() => {
    setEdges((edges) => edges.filter((edge) => edge.id !== id));
  }, [id, setEdges]);

  return (
    <>
      <path
        id={id}
        style={style}
        className="react-flow__edge-path"
        d={edgePath}
        markerEnd={markerEnd}
      />
      <EdgeLabelRenderer>
        <div
          style={{
            position: 'absolute',
            transform: `translate(-50%, -50%) translate(${labelX}px,${labelY}px)`,
            pointerEvents: 'all',
          }}
          className="nodrag nopan"
        >
          <button className="edge-button" onClick={onEdgeClick}>
            ×
          </button>
        </div>
      </EdgeLabelRenderer>
    </>
  );
}

export default memo({EdgeName}Edge);
```

## 경로 유틸리티

| 함수 | 용도 |
|------|------|
| `getBezierPath` | 베지어 곡선 (기본) |
| `getSmoothStepPath` | 부드러운 계단형 |
| `getSimpleBezierPath` | 단순 베지어 |
| `getStraightPath` | 직선 |

## edgeTypes 등록 안내

```typescript
import { ReactFlow } from '@xyflow/react';
import { useMemo } from 'react';
import {EdgeName}Edge from './edges/{EdgeName}Edge';

const edgeTypes = {
  {edgeName}: {EdgeName}Edge,
};

function Flow() {
  const memoizedEdgeTypes = useMemo(() => edgeTypes, []);

  return (
    <ReactFlow
      edgeTypes={memoizedEdgeTypes}
      // ... 기타 props
    />
  );
}
```

## 기본 스타일

```css
.react-flow__edge-path {
  stroke: #b1b1b7;
  stroke-width: 2;
}

.react-flow__edge.selected .react-flow__edge-path {
  stroke: #555;
}

.edge-button {
  width: 20px;
  height: 20px;
  background: #eee;
  border: 1px solid #fff;
  cursor: pointer;
  border-radius: 50%;
  font-size: 14px;
  line-height: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.edge-button:hover {
  background: #ff4444;
  color: white;
}
```
