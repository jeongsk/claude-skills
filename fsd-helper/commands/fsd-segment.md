---
description: Add a segment to existing slice
arguments:
  - name: slice
    description: "Slice path (e.g., features/auth, entities/user)"
    required: true
  - name: segment
    description: "Segment type (ui, api, model, lib, config)"
    required: true
---

# FSD Segment Command

기존 슬라이스에 새 세그먼트를 추가합니다.

## Task

1. 슬라이스 경로 검증:
   - 슬라이스가 존재하는지 확인
   - 경로 형식: `{layer}/{slice-name}`

2. 세그먼트 유효성 검사:
   - 허용: `ui`, `api`, `model`, `lib`, `config`
   - 이미 존재하는 세그먼트인지 확인

3. 세그먼트 생성:

### 세그먼트별 템플릿

**ui:**
```
{slice}/ui/
├── index.ts
└── .gitkeep
```

```typescript
// ui/index.ts
// UI components for this slice
```

**api:**
```
{slice}/api/
├── index.ts
└── types.ts
```

```typescript
// api/index.ts
// API functions for this slice

// api/types.ts
// Request/Response types
export interface ApiResponse<T> {
  data: T;
  error?: string;
}
```

**model:**
```
{slice}/model/
├── index.ts
├── types.ts
└── store.ts (optional)
```

```typescript
// model/types.ts
// Domain types for this slice

// model/index.ts
export type {} from './types';
```

**lib:**
```
{slice}/lib/
└── index.ts
```

```typescript
// lib/index.ts
// Utility functions for this slice
```

**config:**
```
{slice}/config/
├── index.ts
└── constants.ts
```

```typescript
// config/constants.ts
export const CONFIG = {} as const;

// config/index.ts
export * from './constants';
```

4. Public API 업데이트:
   - 슬라이스의 `index.ts`에 새 세그먼트 export 추가

```typescript
// {slice}/index.ts
export {} from './ui';
export {} from './model';
export {} from './api';     // 새로 추가
```

## Examples

```bash
/fsd-segment features/auth api
/fsd-segment entities/user lib
/fsd-segment features/checkout config
```

## Output

- 생성된 파일 목록
- 업데이트된 Public API
- 사용 예시
