# React Flow 엣지 패턴

## 기본 엣지 생성

```typescript
import { Edge } from '@xyflow/react';

const edges: Edge[] = [
  {
    id: 'e1-2',
    source: '1',
    target: '2',
    type: 'smoothstep', // 'default' | 'straight' | 'step' | 'smoothstep'
    animated: true,
    label: 'edge label',
  },
];
```

## 기본 엣지 타입

| 타입 | 설명 |
|------|------|
| `default` (bezier) | 부드러운 곡선 |
| `straight` | 직선 |
| `step` | 90도 각도 계단형 |
| `smoothstep` | 부드러운 계단형 |

## 엣지 속성

```typescript
interface Edge {
  id: string;
  source: string;
  target: string;
  sourceHandle?: string;    // 다중 핸들 시 지정
  targetHandle?: string;
  type?: string;
  animated?: boolean;
  label?: string | ReactNode;
  labelStyle?: CSSProperties;
  labelBgStyle?: CSSProperties;
  style?: CSSProperties;
  markerStart?: EdgeMarker;
  markerEnd?: EdgeMarker;
  data?: any;
}
```

## 커스텀 엣지 기본 템플릿

```typescript
import { memo } from 'react';
import { EdgeProps, getBezierPath } from '@xyflow/react';

function CustomEdge({
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

export default memo(CustomEdge);
```

## 라벨이 있는 커스텀 엣지

```typescript
import { memo } from 'react';
import { EdgeProps, getBezierPath, EdgeLabelRenderer } from '@xyflow/react';

function LabeledEdge({
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
}: EdgeProps) {
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
            pointerEvents: 'all',
          }}
          className="nodrag nopan"
        >
          {data?.label}
        </div>
      </EdgeLabelRenderer>
    </>
  );
}

export default memo(LabeledEdge);
```

## 버튼이 있는 엣지 (삭제/액션)

```typescript
import { memo, useCallback } from 'react';
import {
  EdgeProps,
  getBezierPath,
  EdgeLabelRenderer,
  useReactFlow
} from '@xyflow/react';

function ButtonEdge({
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
          <button
            className="edge-button"
            onClick={onEdgeClick}
          >
            X
          </button>
        </div>
      </EdgeLabelRenderer>
    </>
  );
}

export default memo(ButtonEdge);
```

## 엣지 타입 등록

```typescript
import { ReactFlow } from '@xyflow/react';
import { useMemo } from 'react';

const edgeTypes = {
  custom: CustomEdge,
  labeled: LabeledEdge,
  button: ButtonEdge,
};

function Flow() {
  const memoizedEdgeTypes = useMemo(() => edgeTypes, []);

  return (
    <ReactFlow
      edgeTypes={memoizedEdgeTypes}
      nodes={nodes}
      edges={edges}
    />
  );
}
```

## 경로 유틸리티 함수

```typescript
import {
  getBezierPath,      // 베지어 곡선
  getSmoothStepPath,  // 부드러운 계단형
  getSimpleBezierPath, // 단순 베지어
  getStraightPath,    // 직선
} from '@xyflow/react';

// 사용 예시
const [edgePath, labelX, labelY] = getBezierPath({
  sourceX,
  sourceY,
  sourcePosition,
  targetX,
  targetY,
  targetPosition,
  curvature: 0.25, // 곡률 조정 (선택)
});
```

## 마커 (화살표) 설정

```typescript
const edges: Edge[] = [
  {
    id: 'e1-2',
    source: '1',
    target: '2',
    markerEnd: {
      type: MarkerType.ArrowClosed,
      width: 20,
      height: 20,
      color: '#FF0072',
    },
    style: {
      strokeWidth: 2,
      stroke: '#FF0072',
    },
  },
];
```

## 엣지 스타일링 기본 CSS

```css
.react-flow__edge-path {
  stroke: #b1b1b7;
  stroke-width: 1;
}

.react-flow__edge.selected .react-flow__edge-path {
  stroke: #555;
  stroke-width: 2;
}

.react-flow__edge.animated .react-flow__edge-path {
  stroke-dasharray: 5;
  animation: dashdraw 0.5s linear infinite;
}

@keyframes dashdraw {
  from {
    stroke-dashoffset: 10;
  }
}

.edge-button {
  width: 20px;
  height: 20px;
  background: #eee;
  border: 1px solid #fff;
  cursor: pointer;
  border-radius: 50%;
  font-size: 12px;
  line-height: 1;
}

.edge-button:hover {
  background: #f00;
  color: #fff;
}
```
