---
description: Validate FSD structure and dependency rules
arguments:
  - name: path
    description: "Path to check (default: src)"
    required: false
    default: "src"
  - name: fix
    description: "Suggest fixes for violations"
    required: false
    default: "false"
---

# FSD Check Command

FSD 구조와 의존성 규칙 준수 여부를 검사합니다.

## Task

1. 프로젝트 구조 분석:
   - FSD 레이어 존재 여부 확인
   - 각 레이어 내 슬라이스 구조 확인

2. 의존성 규칙 검사:

### 레이어 간 의존성 검사

```
허용되는 Import 방향:
app → pages → widgets → features → entities → shared
```

각 파일의 import 문을 분석하여:
- 상위 레이어에서 하위 레이어로의 import만 허용
- 역방향 import 탐지 및 보고

### 슬라이스 간 의존성 검사

같은 레이어 내 슬라이스 간 import 탐지:

```typescript
// ❌ 위반: features 내 슬라이스 간 import
// features/checkout/ui/CheckoutForm.tsx
import { useAuth } from '@/features/auth';
```

### Public API 검사

슬라이스 내부에 직접 접근하는 import 탐지:

```typescript
// ❌ 위반: 내부 구조 직접 접근
import { Button } from '@/shared/ui/Button/Button';

// ✅ 올바른 방법
import { Button } from '@/shared/ui';
```

3. 구조 검사:

### 필수 파일 검사

- 각 슬라이스에 `index.ts` (Public API) 존재 여부
- 세그먼트별 `index.ts` 존재 여부

### 네이밍 규칙 검사

- 슬라이스 이름: kebab-case
- 컴포넌트 이름: PascalCase
- 유틸리티 함수: camelCase

4. 결과 리포트:

### 위반 사항 분류

| 심각도 | 유형 | 설명 |
|--------|------|------|
| Error | Layer Violation | 역방향 레이어 import |
| Error | Slice Cross-import | 같은 레이어 슬라이스 간 import |
| Warning | Internal Import | Public API 우회 |
| Info | Missing Index | index.ts 누락 |

### 수정 제안 (--fix)

```
❌ Error: features/checkout/ui/CheckoutForm.tsx
   Line 5: import { useAuth } from '@/features/auth'

   슬라이스 간 직접 import는 금지됩니다.

   ✅ 해결 방법:
   1. 상위 레이어(widgets)에서 조합
   2. Props/Callbacks로 의존성 주입
   3. 공통 로직을 entities 또는 shared로 이동
```

## Output Format

```
FSD Structure Check Report
==========================

📁 Structure Analysis
├── app/          ✅ Valid
├── pages/        ✅ Valid (3 slices)
├── widgets/      ✅ Valid (4 slices)
├── features/     ⚠️ 2 warnings
├── entities/     ✅ Valid (5 slices)
└── shared/       ✅ Valid

🔗 Dependency Analysis
├── Layer violations:     2 errors
├── Slice cross-imports:  1 error
├── Internal imports:     3 warnings
└── Missing public API:   0

📋 Details
...

Summary: 3 errors, 5 warnings
```

## Examples

```bash
/fsd-check
/fsd-check --path src/features
/fsd-check --fix
```
