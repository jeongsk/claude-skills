---
description: Create a new FSD slice
arguments:
  - name: layer
    description: "Layer name (entities, features, widgets, pages)"
    required: true
  - name: name
    description: "Slice name (kebab-case)"
    required: true
  - name: segments
    description: "Segments to create (comma-separated: ui,api,model,lib,config)"
    required: false
    default: "ui,model"
---

# FSD Slice Command

지정된 레이어에 새 슬라이스를 생성합니다.

## Task

1. 레이어 유효성 검사:
   - 허용: `entities`, `features`, `widgets`, `pages`
   - `shared`, `app`은 슬라이스 없이 세그먼트만 사용

2. 슬라이스 이름 검증:
   - kebab-case 형식 확인
   - 기존 슬라이스와 중복 확인

3. 슬라이스 구조 생성:

### 레이어별 기본 구조

**entities:**
```
src/entities/{name}/
├── ui/
│   └── index.ts
├── model/
│   ├── types.ts
│   └── index.ts
├── api/
│   └── index.ts
└── index.ts
```

**features:**
```
src/features/{name}/
├── ui/
│   └── index.ts
├── model/
│   └── index.ts
├── api/
│   └── index.ts
└── index.ts
```

**widgets:**
```
src/widgets/{name}/
├── ui/
│   └── index.ts
└── index.ts
```

**pages:**
```
src/pages/{name}/
├── ui/
│   └── index.ts
└── index.ts
```

4. Public API 템플릿 생성:

```typescript
// {layer}/{name}/index.ts
// Public API for {name} {layer}

// UI exports
export {} from './ui';

// Model exports (if exists)
// export {} from './model';

// API exports (if exists)
// export {} from './api';
```

5. 컴포넌트 템플릿 생성 (옵션):

```typescript
// {layer}/{name}/ui/{PascalName}.tsx
import styles from './{PascalName}.module.css';

interface {PascalName}Props {
  // Define props
}

export function {PascalName}({ }: {PascalName}Props) {
  return (
    <div className={styles.root}>
      {/* {PascalName} */}
    </div>
  );
}
```

## Examples

```bash
/fsd-slice entities user
/fsd-slice features auth --segments ui,api,model
/fsd-slice widgets header
/fsd-slice pages home
```

## Output

- 생성된 파일 목록
- Public API 사용 예시
- Import 방법 안내
