---
description: React Flow 공식 예제를 조회하고 코드를 가져옵니다.
---

# React Flow 예제 조회

공식 예제를 조회하고 관련 코드를 제공합니다.

## 사용 방법

```
/rf-example [카테고리] [예제명]
```

## 카테고리 목록

### nodes (노드 예제)

- custom-node - 기본 커스텀 노드
- update-node - 노드 업데이트
- drag-handle - 드래그 핸들
- easy-connect - 간편 연결
- add-node-on-edge-drop - 엣지 드롭으로 노드 추가
- node-resizer - 노드 리사이징
- node-toolbar - 노드 툴바
- proximity-connect - 근접 연결
- connection-limit - 연결 제한
- shapes - 도형 노드
- stress - 스트레스 테스트

### edges (엣지 예제)

- custom-edge - 커스텀 엣지
- updatable-edge - 업데이트 가능 엣지
- edge-types - 엣지 타입들
- edge-with-button - 버튼이 있는 엣지
- multi-connection-line - 다중 연결선
- simple-floating-edges - 플로팅 엣지
- self-connecting-edge - 자기 연결 엣지

### interaction (상호작용 예제)

- drag-and-drop - 드래그 앤 드롭
- context-menu - 컨텍스트 메뉴
- save-restore - 저장/복원
- validation - 연결 유효성 검사
- undo-redo - 실행 취소/다시 실행
- copy-paste - 복사/붙여넣기
- touch-device - 터치 디바이스
- zoom-transitions - 줌 트랜지션
- prevent-cycles - 사이클 방지

### layout (레이아웃 예제)

- dagre - Dagre 레이아웃
- elkjs - ELK 레이아웃
- d3-force - D3 Force 레이아웃
- horizontal - 가로 레이아웃
- sub-flows - 서브 플로우
- expand-collapse - 확장/축소

### styling (스타일링 예제)

- turbo-flow - Turbo 스타일
- tailwind - Tailwind CSS
- dark-mode - 다크 모드
- styled-components - Styled Components

## 동작 지침

1. 카테고리와 예제명 파싱
2. WebFetch로 예제 페이지 조회:
   - `https://r.jina.ai/https://reactflow.dev/examples/{category}/{example}`
3. 예제 코드 추출 및 설명 제공
4. 프로젝트에 적용하는 방법 안내

## URL 패턴

```
https://r.jina.ai/https://reactflow.dev/examples/{category}/{example-name}
```

## 예시

```
/rf-example nodes custom-node
-> https://r.jina.ai/https://reactflow.dev/examples/nodes/custom-node 조회

/rf-example layout dagre
-> https://r.jina.ai/https://reactflow.dev/examples/layout/dagre 조회

/rf-example interaction drag-and-drop
-> https://r.jina.ai/https://reactflow.dev/examples/interaction/drag-and-drop 조회
```

## 카테고리 전체 조회

카테고리만 지정하면 해당 카테고리의 모든 예제 목록 표시:

```
/rf-example nodes
-> https://r.jina.ai/https://reactflow.dev/examples/nodes 조회
```

## 실행

WebFetch 도구를 사용하여 예제 페이지를 가져오고 다음을 제공:

1. 예제 개요 및 목적
2. 핵심 코드 (컴포넌트, 훅 사용법)
3. 주요 패턴 및 기법 설명
4. 프로젝트 적용 방법
