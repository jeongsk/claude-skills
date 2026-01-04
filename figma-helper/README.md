# Figma Helper Plugin

Figma Dev Mode MCP 도구를 활용한 디자인-코드 변환 지원 플러그인입니다.

## 기능

- **디자인 컨텍스트 분석**: Figma 디자인 요소의 구조, 스타일, 레이아웃 정보 추출
- **코드 생성**: 디자인을 React + Tailwind CSS 코드로 변환
- **디자인 토큰 조회**: 색상, 간격, 타이포그래피 변수 확인
- **스크린샷 캡처**: 디자인 화면 캡처 및 레이아웃 검증
- **컴포넌트 매핑**: Figma 노드와 코드 컴포넌트 연결

## MCP 도구

이 플러그인은 다음 Figma MCP 도구 사용을 지원합니다:

| 도구 | 설명 |
|------|------|
| `get_design_context` | 디자인 컨텍스트 조회 및 코드 생성 (핵심 도구) |
| `get_metadata` | 요소 메타데이터 조회 (XML 형식) |
| `get_screenshot` | 화면 스크린샷 캡처 |
| `get_variable_defs` | 디자인 토큰/변수 조회 |
| `get_code_connect_map` | 코드 컴포넌트 매핑 조회 |
| `add_code_connect_map` | 코드 컴포넌트 매핑 추가 |
| `create_design_system_rules` | 디자인 시스템 규칙 생성 |
| `get_figjam` | FigJam 다이어그램 조회 |

## 설치

플러그인 설치 시 `.mcp.json` 파일을 통해 MCP 서버가 자동으로 설정됩니다.

```bash
# 플러그인 설치
claude plugins add figma-helper
```

## 사용 방법

### 디자인 분석

Figma에서 요소를 선택한 후:

```
"이 디자인의 구조를 분석해줘"
"선택한 컴포넌트의 스타일 정보 알려줘"
```

### 코드 생성

```
"이 버튼을 React 컴포넌트로 만들어줘"
"선택한 카드 디자인을 코드로 변환해줘"
```

### 디자인 토큰 확인

```
"이 디자인의 색상 변수를 확인해줘"
"사용된 타이포그래피 스타일 알려줘"
```

### 레이아웃 검증

```
"디자인 스크린샷을 캡처해줘"
"구현 결과가 디자인과 일치하는지 확인해줘"
```

## 워크플로우

### 권장 순서

1. `get_design_context` - 전체 구조 파악 + 코드 생성
2. `get_metadata` - 세부 요소 확인 (필요시)
3. `get_variable_defs` - 디자인 토큰 확인 (필요시)
4. 코드 최적화 및 프로젝트 스타일 적용

### 레이아웃 검증 순서

1. `get_screenshot` - 원본 디자인 캡처
2. `get_design_context` - 코드 생성
3. 구현 결과와 스크린샷 비교

## 요구사항

- Figma 데스크톱 앱 실행
- Figma Dev Mode 활성화
- Figma Dev Mode MCP 서버 실행 (포트 3845)

## 구조

```
figma-helper/
├── .claude-plugin/
│   └── plugin.json
├── .mcp.json                # MCP 서버 설정
├── skills/
│   └── converting-figma-designs/
│       ├── SKILL.md
│       └── references/
│           ├── mcp-tools.md
│           ├── workflows.md
│           └── troubleshooting.md
└── README.md
```

## 라이선스

MIT
