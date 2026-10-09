#!/usr/bin/env python3
"""Write the competitive-programming notebook site."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = "https://github.com/lamng3/competitive-programming-notebook/blob/main"
LEVELS = ["silver", "gold", "platinum", "advanced"]

NAV = [
    ("index.html", "Overview"),
    ("contest.html", "Contest"),
    ("data-structures.html", "Data structures"),
    ("graph.html", "Graph"),
    ("math.html", "Math"),
    ("strings.html", "Strings"),
    ("dynamic-programming.html", "Dynamic programming"),
    ("databases.html", "Databases"),
]

FOOTER = (
    "Notebook notes, grouped like KACTL. "
    f'Code: <a href="https://github.com/lamng3/competitive-programming-notebook">competitive programming notebook</a>.'
)


def link(path, label):
    return f'<a href="{REPO}/{path}"><code>{label}</code></a>'


def nav_html(current):
    parts = ['<a class="brand-desk" href="index.html">notebook</a>']
    for href, label in NAV:
        attr = ' aria-current="page"' if href == current else ""
        parts.append(f'<a href="{href}"{attr}>{label}</a>')
    return "".join(parts)


def page(filename, title, description, kicker, lede, body):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — notebook</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip" href="#content">Skip to content</a>
<header class="top">
  <a class="brand" href="index.html">notebook</a>
  <label class="nav-button" for="nav-toggle">Menu</label>
</header>
<input id="nav-toggle" class="nav-toggle" type="checkbox">
<div class="layout">
<nav class="nav">
{nav_html(filename)}
</nav>
<main id="content">
<p class="kicker">{kicker}</p>
<h1>{title}</h1>
<p class="lede">{lede}</p>
{body}
</main>
</div>
<footer class="site">{FOOTER}</footer>
</body>
</html>
"""
    (ROOT / filename).write_text(html, encoding="utf-8")


def item_html(item):
    # (path, name, blurb) or (path, name, blurb, [sub items]) for an indented list under it
    path, name, blurb, *sub = item
    html = f"<li>{link(path, name)}. {blurb}"
    if sub:
        html += "\n<ul>\n" + "\n".join(item_html(s) for s in sub[0]) + "\n</ul>\n"
    return html + "</li>"


def section(title, level, items):
    tag = f' <span class="tag">[{level}]</span>' if level else ""
    rows = "\n".join(item_html(item) for item in items)
    return f"<h2>{title}{tag}</h2>\n<ul>\n{rows}\n</ul>\n"


# category, level, title, items
TOPICS = [
    (
        "contest",
        "",
        "Starters",
        [
            ("templates/contest.cpp", "contest.cpp", "Default contest file."),
            ("templates/leetcode.cpp", "leetcode.cpp", "LeetCode method stub."),
            ("templates/minimal.cpp", "minimal.cpp", "Shortest starter."),
            ("templates/oi.cpp", "oi.cpp", "OI starter."),
            ("python/template.py", "template.py", "Python starter."),
        ],
    ),
    (
        "contest",
        "",
        "Tools",
        [
            ("tools/cpnew.py", "cpnew", "Copy a template into a new file."),
            ("tools/cpgen.py", "cpgen", "Fetch a LeetCode problem and write the stub."),
            ("tools/cptest.py", "cptest", "Run a solution against cached examples."),
        ],
    ),
    (
        "data-structures",
        "silver",
        "Coordinate compression",
        [
            (
                "notebook/utils/CoordinateCompression.h",
                "CoordinateCompression.h",
                "Sort unique values and map them back to ranks.",
            ),
        ],
    ),
    (
        "data-structures",
        "gold",
        "Fenwick tree",
        [
            (
                "notebook/data_structures/1d_range_query/FenwickTree.h",
                "FenwickTree.h",
                "Prefix sums with point updates.",
            ),
        ],
    ),
    (
        "data-structures",
        "gold",
        "Segment tree",
        [
            (
                "notebook/data_structures/1d_range_query/SegmentTree.h",
                "SegmentTree.h",
                "Recursive segment tree.",
            ),
            (
                "notebook/data_structures/1d_range_query/IterativeSegmentTree.h",
                "IterativeSegmentTree.h",
                "Iterative segment tree.",
            ),
        ],
    ),
    (
        "data-structures",
        "platinum",
        "Lazy segment tree",
        [
            (
                "notebook/data_structures/rurq/LazySegmentTree.h",
                "LazySegmentTree.h",
                "Segment tree with lazy range updates.",
            ),
        ],
    ),
    (
        "data-structures",
        "platinum",
        "Sparse segment tree",
        [
            (
                "notebook/data_structures/rurq/SparseSegmentTree.h",
                "SparseSegmentTree.h",
                "A segment tree that allocates only visited nodes.",
            ),
        ],
    ),
    (
        "data-structures",
        "platinum",
        "Mo's algorithm",
        [
            ("notebook/data_structures/1d_range_query/Mo.h", "Mo.h", "Offline range queries in blocks."),
            ("contests/leetcode/solve/mo_algorithm", "mo_algorithm/", "A solved Mo problem."),
        ],
    ),
    (
        "data-structures",
        "platinum",
        "Square root decomposition",
        [
            (
                "notebook/data_structures/1d_range_query/SRD.h",
                "SRD.h",
                "Blocks over a one-dimensional array.",
            ),
        ],
    ),
    (
        "data-structures",
        "advanced",
        "Persistent segment tree",
        [
            (
                "notebook/data_structures/rurq/PersistentSegmentTree.h",
                "PersistentSegmentTree.h",
                "Persistent sparse segment tree.",
            ),
        ],
    ),
    (
        "graph",
        "silver",
        "Compressed sparse row",
        [
            (
                "notebook/data_structures/compress/CSR.h",
                "CSR.h",
                "Adjacency stored as offsets and edges.",
            ),
        ],
    ),
    (
        "graph",
        "gold",
        "Disjoint set union",
        [
            ("notebook/graphs/dsu/DSU.h", "DSU.h", "Parent and size, with path compression."),
            ("python/graphs/dsu/DSU.py", "DSU.py", "The same structure in Python."),
            ("notebook/examples/graphs/dsu/323.cpp", "323.cpp", "A worked DSU problem."),
        ],
    ),
    (
        "graph",
        "gold",
        "Euler tour",
        [
            ("notebook/trees/euler_tour/EulerTour.h", "EulerTour.h", "Entry and exit times on a tree."),
            ("contests/leetcode/solve/euler_tour", "euler_tour/", "Solved Euler-tour problems."),
        ],
    ),
    (
        "graph",
        "platinum",
        "Binary lifting",
        [
            ("contests/leetcode/solve/binary_lifting", "binary_lifting/", "Binary lifting solutions."),
        ],
    ),
    (
        "graph",
        "platinum",
        "Small to large",
        [
            (
                "contests/leetcode/solve/small_to_large_merging",
                "small_to_large_merging/",
                "Small-to-large merging solutions.",
            ),
        ],
    ),
    (
        "graph",
        "advanced",
        "DSU rollback",
        [
            ("notebook/graphs/dsu/DSURollback.h", "DSURollback.h", "Disjoint set union that can undo unions."),
            ("contests/leetcode/solve/dsu_rollback", "dsu_rollback/", "A solved rollback problem."),
        ],
    ),
    (
        "graph",
        "advanced",
        "Strongly connected components",
        [
            ("contests/leetcode/solve/kosaraju", "kosaraju/", "Kosaraju solutions."),
        ],
    ),
    (
        "graph",
        "advanced",
        "Eulerian path",
        [
            ("contests/leetcode/solve/eulerian_path", "eulerian_path/", "Eulerian-path solutions."),
        ],
    ),
    (
        "math",
        "gold",
        "Modular arithmetic",
        [
            ("notebook/math/modular_arithmetic/ModFact.h", "ModFact.h", "Factorials and powers modulo 10^9+7."),
            ("notebook/math/modular_arithmetic/ModInv.h", "ModInv.h", "Modular inverse by binary exponentiation."),
            ("notebook/examples/modular_arithmetic/3881.cpp", "3881.cpp", "A worked modular problem."),
        ],
    ),
    (
        "strings",
        "gold",
        "Rolling hash",
        [
            ("notebook/strings/rolling_hash/rollinghash.h", "rollinghash.h", "Forward and backward rolling hash."),
            ("python/strings/rolling_hash/RollingHash.py", "RollingHash.py", "The same hash in Python."),
        ],
    ),
    (
        "strings",
        "gold",
        "Trie",
        [
            ("contests/leetcode/solve/trie", "trie/", "Trie solutions."),
        ],
    ),
    (
        "dynamic-programming",
        "gold",
        "Dynamic programming",
        [
            ("notebook/examples/dynamic_programming/3418.cpp", "3418.cpp", "One DP writeup."),
            ("contests/usaco/dp", "usaco/dp/", "DP solutions."),
            ("contests/leetcode/solve/dp_on_tree", "dp_on_tree/", "Tree DP solutions."),
            ("contests/leetcode/solve/lis", "lis/", "Longest increasing subsequence."),
        ],
    ),
    (
        "databases",
        "advanced",
        "Filters",
        [
            (
                "notebook/databases/data_structures/bloomfilter.h",
                "bloomfilter.h",
                "Bloom filter.",
                [("python/databases/data_structures/BloomFilter.py", "BloomFilter.py", "The same filter in Python.")],
            ),
            (
                "notebook/databases/data_structures/countminsketch.h",
                "countminsketch.h",
                "Count-min sketch with seeded hashes, merge, and top k.",
                [("python/databases/data_structures/CountMinSketch.py", "CountMinSketch.py", "The same sketch in Python.")],
            ),
            (
                "notebook/databases/data_structures/cuckoofilter.h",
                "cuckoofilter.h",
                "Cuckoo filter with fingerprints, kicks, and deletes.",
                [("python/databases/data_structures/CuckooFilter.py", "CuckooFilter.py", "The same filter in Python.")],
            ),
        ],
    ),
    (
        "databases",
        "advanced",
        "Hash",
        [
            (
                "notebook/databases/data_structures/utils/hash.h",
                "hash.h",
                "String hashes, mixers, and a rolling hash.",
                [("python/databases/data_structures/utils/hash.py", "hash.py", "The string hashes in Python.")],
            ),
        ],
    ),
    (
        "databases",
        "advanced",
        "Skip list",
        [
            (
                "notebook/databases/data_structures/skiplist.h",
                "skiplist.h",
                "Skip list.",
                [("python/databases/data_structures/Skiplist.py", "Skiplist.py", "The same structure in Python.")],
            ),
        ],
    ),
    (
        "databases",
        "advanced",
        "Caches",
        [
            ("notebook/databases/eviction/fifo.h", "fifo.h", "FIFO eviction."),
            ("notebook/databases/eviction/lru.h", "lru.h", "LRU eviction."),
            ("notebook/databases/eviction/lfu.h", "lfu.h", "LFU eviction."),
            ("notebook/databases/eviction/lru-2q.h", "lru-2q.h", "LRU-2Q eviction."),
        ],
    ),
]

PAGES = {
    "contest": (
        "contest.html",
        "Contest",
        "Starters and the cpnew, cpgen, and cptest tools.",
        "contest",
        "Files you copy at the start of a problem.",
    ),
    "data-structures": (
        "data-structures.html",
        "Data structures",
        "Range trees, Mo, square root, and persistence.",
        "data-structures",
        "Ordered from silver through advanced.",
    ),
    "graph": (
        "graph.html",
        "Graph",
        "Adjacency, DSU, tree tours, jumps, and connectivity.",
        "graph",
        "Ordered from silver through advanced.",
    ),
    "math": (
        "math.html",
        "Math",
        "Modular factorials and inverses.",
        "math",
        "Gold modular snippets.",
    ),
    "strings": (
        "strings.html",
        "Strings",
        "Rolling hash and trie.",
        "strings",
        "Gold string snippets.",
    ),
    "dynamic-programming": (
        "dynamic-programming.html",
        "Dynamic programming",
        "DP writeups, tree DP, and longest increasing subsequence.",
        "dynamic-programming",
        "Gold dynamic programming snippets.",
    ),
    "databases": (
        "databases.html",
        "Databases",
        "Bloom and cuckoo filters, hashes, a skip list, and cache eviction.",
        "databases",
        "Filters, hashes, a skip list, and cache eviction.",
    ),
}


def main():
    for old in [
        "general.html",
        "bronze.html",
        "silver.html",
        "gold.html",
        "plat.html",
        "advanced.html",
        "various.html",
    ]:
        path = ROOT / old
        if path.exists():
            path.unlink()

    by_cat = {key: [] for key in PAGES}
    for cat, level, title, items in TOPICS:
        by_cat[cat].append((LEVELS.index(level) if level else -1, title, level, items))

    cards = []
    blurbs = {
        "contest": "Starters and tools.",
        "data-structures": "Trees, Mo, and persistence.",
        "graph": "DSU, tours, jumps, and connectivity.",
        "math": "Modular arithmetic.",
        "strings": "Hashing and tries.",
        "dynamic-programming": "Writeups, tree DP, and LIS.",
        "databases": "Filters, hashes, a skip list, and caches.",
    }
    for key, (filename, title, _desc, _kicker, _lede) in PAGES.items():
        cards.append(
            f'<a class="card" href="{filename}"><strong>{title}</strong><span>{blurbs[key]}</span></a>'
        )

    page(
        "index.html",
        "Overview",
        "Competitive programming templates grouped by topic, with a level tag on each one.",
        "Notebook",
        "Snippets from the competitive programming notebook, grouped the way KACTL groups them. A tag on each topic is the level.",
        """
<nav class="toc"><strong>On this page</strong><ol><li><a href="#topics">Topics</a></li></ol></nav>
<p>Within a topic page, silver comes before gold, then platinum, then advanced.</p>
<h2 id="topics">Topics</h2>
<div class="cards">
"""
        + "\n".join(cards)
        + "\n</div>\n",
    )

    for key, (filename, title, description, kicker, lede) in PAGES.items():
        body = "".join(
            section(name, level, items)
            for _rank, name, level, items in sorted(by_cat[key], key=lambda row: (row[0], row[1]))
        )
        if key == "contest":
            body += "<p><code>cpbuild</code> compiles a file with warnings and sanitizers. It is a shell function in the repository README.</p>\n"
        page(filename, title, description, kicker, lede, body)


if __name__ == "__main__":
    main()
