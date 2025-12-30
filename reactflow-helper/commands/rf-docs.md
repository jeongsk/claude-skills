---
description: React Flow 공식 문서를 조회합니다. 특정 주제나 API에 대한 최신 정보를 가져옵니다.
---

# React Flow 문서 조회

사용자가 요청한 React Flow 관련 문서를 WebFetch를 통해 조회합니다.

## 사용 방법

```
/rf-docs [주제]
```

## 지원 주제

- `api` - API 레퍼런스 전체
- `hooks` - React Flow 훅 목록 (useReactFlow, useNodes, useEdges 등)
- `components` - 컴포넌트 목록 (Handle, NodeResizer, Background 등)
- `types` - TypeScript 타입 정의
- `examples` - 예제 목록
- `nodes` - 노드 관련 문서 (커스텀 노드 포함)
- `edges` - 엣지 관련 문서 (커스텀 엣지 포함)
- `layout` - 레이아웃 관련 문서
- `ui` - UI 컴포넌트 라이브러리

## 동작 지침

1. 사용자의 요청을 분석하여 적절한 주제 결정
2. 아래 URL 매핑에 따라 WebFetch 도구 호출
3. 조회된 문서에서 관련 정보 요약 및 코드 예제 제공

## URL 매핑

| 주제 | URL |
|------|-----|
| api | `https://r.jina.ai/https://reactflow.dev/api-reference` |
| hooks | `https://r.jina.ai/https://reactflow.dev/api-reference/hooks` |
| components | `https://r.jina.ai/https://reactflow.dev/api-reference/components` |
| types | `https://r.jina.ai/https://reactflow.dev/api-reference/types` |
| examples | `https://r.jina.ai/https://reactflow.dev/examples` |
| nodes | `https://r.jina.ai/https://reactflow.dev/learn/customization/custom-nodes` |
| edges | `https://r.jina.ai/https://reactflow.dev/learn/customization/custom-edges` |
| layout | `https://r.jina.ai/https://reactflow.dev/examples/layout` |
| ui | `https://r.jina.ai/https://reactflow.dev/ui` |

## 세부 문서 URL 패턴

특정 API나 컴포넌트에 대한 상세 정보가 필요한 경우:

- 특정 훅: `https://r.jina.ai/https://reactflow.dev/api-reference/hooks/{hook-name}`
  - 예: useReactFlow, useNodes, useEdges, useNodesState, useEdgesState
- 특정 컴포넌트: `https://r.jina.ai/https://reactflow.dev/api-reference/components/{component-name}`
  - 예: handle, node-resizer, node-toolbar, background, controls, mini-map
- 특정 예제: `https://r.jina.ai/https://reactflow.dev/examples/{category}/{example-name}`

## 실행

WebFetch 도구를 사용하여 해당 URL의 문서를 가져오고, 사용자에게 다음을 제공합니다:

1. 요청한 주제에 대한 개요
2. 핵심 API/속성/메서드 목록
3. 관련 코드 예제
4. 추가 참고 링크
