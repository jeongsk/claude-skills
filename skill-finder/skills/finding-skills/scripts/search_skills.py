#!/usr/bin/env python3
"""
SkillsMP API를 호출하여 Claude Code 스킬을 검색하는 스크립트.

사용법:
    python search_skills.py <검색어> [--limit N] [--page N] [--sort stars|recent|name]

예시:
    python search_skills.py "pdf"
    python search_skills.py "git commit" --limit 5
    python search_skills.py "image processing" --sort recent
"""

import argparse
import json
import sys
import urllib.request
import urllib.parse
import urllib.error
from typing import Optional


def search_skills(
    query: str,
    limit: int = 10,
    page: int = 1,
    sort_by: str = "stars"
) -> dict:
    """
    SkillsMP API를 호출하여 스킬을 검색합니다.

    Args:
        query: 검색어 (영어 권장)
        limit: 반환할 결과 수 (기본값: 10)
        page: 페이지 번호 (기본값: 1)
        sort_by: 정렬 기준 (stars, recent, name)

    Returns:
        검색 결과를 담은 딕셔너리
    """
    base_url = "https://skillsmp.com/api/skills"

    params = {
        "page": page,
        "limit": limit,
        "sortBy": sort_by,
        "marketplaceOnly": "false",
        "source": "home",
        "search": query
    }

    url = f"{base_url}?{urllib.parse.urlencode(params)}"

    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Claude-Code-Skill-Finder/1.0",
                "Accept": "application/json"
            }
        )

        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
            return format_response(data, query)

    except urllib.error.HTTPError as e:
        return {
            "success": False,
            "error": f"HTTP Error: {e.code} - {e.reason}",
            "query": query
        }
    except urllib.error.URLError as e:
        return {
            "success": False,
            "error": f"URL Error: {str(e.reason)}",
            "query": query
        }
    except json.JSONDecodeError as e:
        return {
            "success": False,
            "error": f"JSON Parse Error: {str(e)}",
            "query": query
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Unexpected Error: {str(e)}",
            "query": query
        }


def format_response(data: dict, query: str) -> dict:
    """
    API 응답에서 필요한 정보만 추출하여 간결한 형태로 반환합니다.

    Args:
        data: SkillsMP API 원본 응답
        query: 검색어

    Returns:
        간결화된 응답 딕셔너리
    """
    skills = data.get("skills", [])
    pagination = data.get("pagination", {})

    formatted_skills = []
    for skill in skills:
        formatted_skill = {
            "name": skill.get("name", ""),
            "author": skill.get("author", ""),
            "description": skill.get("description", ""),
            "stars": skill.get("stars", 0),
            "githubUrl": skill.get("githubUrl", ""),
            "hasMarketplace": skill.get("hasMarketplace", False),
            "updatedAt": skill.get("updatedAt", 0)
        }
        formatted_skills.append(formatted_skill)

    return {
        "success": True,
        "query": query,
        "total": pagination.get("total", 0),
        "page": pagination.get("page", 1),
        "totalPages": pagination.get("totalPages", 1),
        "hasNext": pagination.get("hasNext", False),
        "skills": formatted_skills
    }


def format_output(result: dict, output_format: str = "json") -> str:
    """
    결과를 지정된 형식으로 포맷팅합니다.

    Args:
        result: 검색 결과 딕셔너리
        output_format: 출력 형식 (json, text)

    Returns:
        포맷팅된 문자열
    """
    if output_format == "json":
        return json.dumps(result, ensure_ascii=False, indent=2)

    # text 형식
    if not result.get("success"):
        return f"Error: {result.get('error', 'Unknown error')}"

    lines = []
    lines.append(f"검색어: {result['query']}")
    lines.append(f"총 결과: {result['total']}개 (페이지 {result['page']}/{result['totalPages']})")
    lines.append("")

    for i, skill in enumerate(result["skills"], 1):
        lines.append(f"## {i}. {skill['name']}")
        lines.append(f"   작성자: {skill['author']}")
        lines.append(f"   설명: {skill['description']}")
        lines.append(f"   인기도: ⭐ {skill['stars']}")
        lines.append(f"   마켓플레이스: {'있음' if skill['hasMarketplace'] else '없음'}")
        lines.append(f"   GitHub: {skill['githubUrl']}")
        lines.append("")

    if result["hasNext"]:
        lines.append(f"더 많은 결과가 있습니다. --page {result['page'] + 1} 옵션을 사용하세요.")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="SkillsMP API에서 Claude Code 스킬을 검색합니다."
    )
    parser.add_argument(
        "query",
        type=str,
        help="검색어 (영어 권장)"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="반환할 결과 수 (기본값: 10)"
    )
    parser.add_argument(
        "--page",
        type=int,
        default=1,
        help="페이지 번호 (기본값: 1)"
    )
    parser.add_argument(
        "--sort",
        type=str,
        default="stars",
        choices=["stars", "recent", "name"],
        help="정렬 기준 (기본값: stars)"
    )
    parser.add_argument(
        "--format",
        type=str,
        default="json",
        choices=["json", "text"],
        help="출력 형식 (기본값: json)"
    )

    args = parser.parse_args()

    result = search_skills(
        query=args.query,
        limit=args.limit,
        page=args.page,
        sort_by=args.sort
    )

    print(format_output(result, args.format))


if __name__ == "__main__":
    main()
