# React Flow Helper Plugin

React Flow 라이브러리를 사용한 노드 기반 UI 개발을 지원하는 Claude Code 플러그인입니다.

## 사용 방법

### 커맨드

#### `/rf-docs` - 문서 조회

React Flow 공식 문서를 조회합니다.

```
/rf-docs api          # API 레퍼런스
/rf-docs hooks        # 훅 목록 (useReactFlow, useNodes 등)
/rf-docs components   # 컴포넌트 목록
/rf-docs nodes        # 커스텀 노드 가이드
/rf-docs edges        # 커스텀 엣지 가이드
/rf-docs layout       # 레이아웃 예제
/rf-docs examples     # 전체 예제 목록
/rf-docs ui           # UI 컴포넌트 라이브러리
```

#### `/rf-node` - 노드 생성

커스텀 노드 컴포넌트를 생성합니다.

```
/rf-node MyCustomNode                    # 기본 노드
/rf-node MyCustomNode --resizable        # 리사이징 가능 노드
/rf-node MyCustomNode --toolbar          # 툴바가 있는 노드
/rf-node MyCustomNode --multiple-handles # 다중 핸들 노드
```

#### `/rf-edge` - 엣지 생성

커스텀 엣지 컴포넌트를 생성합니다.

```
/rf-edge MyCustomEdge                 # 기본 엣지
/rf-edge MyCustomEdge --label         # 라벨이 있는 엣지
/rf-edge MyCustomEdge --button        # 삭제 버튼이 있는 엣지
/rf-edge MyCustomEdge --type smoothstep  # 특정 경로 타입
```

#### `/rf-example` - 예제 조회

공식 예제를 조회합니다.

```
/rf-example nodes                     # 노드 예제 목록
/rf-example nodes custom-node         # 특정 예제 상세
/rf-example edges edge-with-button    # 버튼 엣지 예제
/rf-example layout dagre              # Dagre 레이아웃 예제
/rf-example interaction drag-and-drop # 드래그 앤 드롭 예제
```

#### `/rf-setup` - 프로젝트 설정

새 프로젝트에 React Flow를 설정합니다.

```
/rf-setup                    # 기본 TypeScript 설정
/rf-setup --tailwind         # Tailwind CSS 통합
/rf-setup --zustand          # Zustand 상태 관리 포함
```

### 스킬 (자동 활성화)

React Flow 관련 질문을 하면 `reactflow-dev` 스킬이 자동으로 활성화되어 최신 문서를 참조합니다:

```
"useReactFlow 훅 사용법 알려줘"
"커스텀 노드에서 리사이징 기능 추가하는 방법"
"Dagre 레이아웃 적용하는 방법"
```

### 에이전트

복잡한 React Flow 구현이 필요한 경우 `reactflow-specialist` 에이전트가 지원합니다:

- 대규모 노드 그래프 아키텍처 설계
- 성능 최적화 전략
- 상태 관리 설계 (Zustand/Redux)
- TypeScript 타입 통합
