---
description: Fetch FSD documentation
arguments:
  - name: topic
    description: "Documentation topic (overview, layers, slices, segments, rules, migration, examples)"
    required: false
    default: "overview"
---

# FSD Docs Command

Feature-Sliced Design 공식 문서를 조회합니다.

## Task

지정된 토픽에 해당하는 FSD 공식 문서를 가져와 요약합니다.

### 토픽별 문서 URL

| 토픽 | URL |
|------|-----|
| overview | https://feature-sliced.design/kr/docs/get-started/overview |
| layers | https://feature-sliced.design/kr/docs/reference/layers |
| slices | https://feature-sliced.design/kr/docs/reference/slices-segments |
| segments | https://feature-sliced.design/kr/docs/reference/slices-segments |
| rules | https://feature-sliced.design/kr/docs/reference/isolation |
| migration | https://feature-sliced.design/kr/docs/guides/migration |
| examples | https://feature-sliced.design/kr/docs/guides/examples |
| tutorial | https://feature-sliced.design/kr/docs/get-started/tutorial |

### WebFetch 사용

```
WebFetch를 사용하여 해당 URL의 문서를 가져옵니다.
```

## Topic Descriptions

### overview
FSD의 핵심 개념과 목표, 기본 구조 소개

### layers
7개 레이어(app, pages, widgets, features, entities, shared)의 역할과 책임

### slices
슬라이스의 개념, 네이밍 규칙, 구조화 방법

### segments
세그먼트(ui, api, model, lib, config)의 역할과 조직 방법

### rules
의존성 규칙, Public API, 격리 원칙

### migration
기존 프로젝트를 FSD로 마이그레이션하는 전략

### examples
실제 FSD 적용 사례와 예제 프로젝트

### tutorial
단계별 FSD 시작 가이드

## Examples

```bash
/fsd-docs                    # overview 조회
/fsd-docs layers             # 레이어 문서
/fsd-docs rules              # 의존성 규칙
/fsd-docs migration          # 마이그레이션 가이드
```

## Output

- 문서 요약
- 핵심 포인트 하이라이트
- 관련 명령어 추천 (해당 시)
