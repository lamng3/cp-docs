#!/usr/bin/env python3
"""Write the competitive-programming notebook site."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = "https://github.com/lamng3/competitive-programming-setup/blob/main"

NAV = [
    ("index.html", "Overview"),
    ("general.html", "General"),
    ("bronze.html", "Bronze"),
    ("silver.html", "Silver"),
    ("gold.html", "Gold"),
    ("plat.html", "Platinum"),
    ("advanced.html", "Advanced"),
]

FOOTER = (
    "Notebook notes. Divisions follow the USACO Guide folders "
    '<code>1_General</code> through <code>6_Advanced</code>. '
    f'Code: <a href="{REPO.rsplit("/blob", 1)[0]}">competitive-programming-setup</a>.'
)


def link(path, label=None):
    label = label or path
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


def topic(heading, guide, items):
    rows = "\n".join(
        f"<li>{link(path, name)}. {blurb}</li>" for path, name, blurb in items
    )
    guide_line = f"<p>USACO Guide module: <code>{guide}</code>.</p>" if guide else ""
    return f"<h2>{heading}</h2>\n{guide_line}\n<ul>\n{rows}\n</ul>\n"


def main():
    page(
        "index.html",
        "Overview",
        "Competitive programming templates and notebook snippets, filed by USACO division.",
        "Notebook",
        "Templates and snippets from competitive-programming-setup, filed the way the USACO Guide files its modules.",
        """
<nav class="toc"><strong>On this page</strong><ol><li><a href="#divisions">Divisions</a></li><li><a href="#layout">Layout</a></li></ol></nav>
<p>The guide uses <code>1_General</code>, <code>2_Bronze</code>, <code>3_Silver</code>, <code>4_Gold</code>, <code>5_Plat</code>, and <code>6_Advanced</code>. Each page below keeps that order and lists only the snippets in this repository.</p>
<h2 id="divisions">Divisions</h2>
<div class="cards">
<a class="card" href="general.html"><strong>General</strong><span>Contest, LeetCode, minimal, and OI starters, plus cpnew, cpgen, and cptest.</span></a>
<a class="card" href="bronze.html"><strong>Bronze</strong><span>No separate snippet. Starters live in General.</span></a>
<a class="card" href="silver.html"><strong>Silver</strong><span>Coordinate compression and compressed sparse row.</span></a>
<a class="card" href="gold.html"><strong>Gold</strong><span>Fenwick and segment trees, DSU, hashing, modular arithmetic, Euler tour, DP, LIS, trie.</span></a>
<a class="card" href="plat.html"><strong>Platinum</strong><span>Lazy and sparse segment trees, Mo, square root, binary lifting, small-to-large.</span></a>
<a class="card" href="advanced.html"><strong>Advanced</strong><span>Persistent trees, SCC, Eulerian paths, DSU rollback, and cache structures.</span></a>
</div>
<h2 id="layout">Layout</h2>
<ul>
<li><code>templates/</code> contest starters.</li>
<li><code>notebook/</code> C++ snippets.</li>
<li><code>python/</code> the same ideas in Python.</li>
<li><code>contests/</code> solved problems, grouped by topic where a folder exists.</li>
</ul>
""",
    )
    page(
        "general.html",
        "General",
        "Contest starters and the cpnew, cpgen, and cptest tools.",
        "1_General",
        "Starters and tools. These are not tied to one division.",
        topic(
            "Starters",
            "Generic_Code",
            [
                ("templates/contest.cpp", "contest.cpp", "Default contest file."),
                ("templates/leetcode.cpp", "leetcode.cpp", "LeetCode method stub."),
                ("templates/minimal.cpp", "minimal.cpp", "Shortest starter."),
                ("templates/oi.cpp", "oi.cpp", "OI starter."),
                ("python/template.py", "template.py", "Python starter."),
            ],
        )
        + topic(
            "Tools",
            "Running_Code_Locally",
            [
                ("tools/cpnew.py", "cpnew", "Copy a template into a new file."),
                ("tools/cpgen.py", "cpgen", "Fetch a LeetCode problem and write the stub."),
                ("tools/cptest.py", "cptest", "Run a solution against cached examples."),
            ],
        )
        + "<p><code>cpbuild</code> compiles a file with warnings and sanitizers. It is a shell function in the repository README, not a file in <code>tools/</code>.</p>",
    )
    page(
        "bronze.html",
        "Bronze",
        "Bronze has no separate notebook snippet.",
        "2_Bronze",
        "Simulation, complete search, and the introductory modules stay in the guide. This repository does not keep a bronze-only template.",
        """
<p>Use a starter from <a href="general.html">General</a> for a bronze problem. The first snippets in the notebook are silver and gold.</p>
""",
    )
    page(
        "silver.html",
        "Silver",
        "Coordinate compression and compressed sparse row.",
        "3_Silver",
        "Two silver snippets. Prefix sums, two pointers, and flood fill are not separate files here.",
        topic(
            "Sorting",
            "Sorting_Custom",
            [
                (
                    "notebook/utils/CoordinateCompression.h",
                    "CoordinateCompression.h",
                    "Sort unique values and map them back to ranks.",
                ),
            ],
        )
        + topic(
            "Graph traversal",
            "Graph_Traversal",
            [
                (
                    "notebook/data_structures/compress/CSR.h",
                    "CSR.h",
                    "Compressed sparse row for an adjacency list.",
                ),
            ],
        ),
    )
    page(
        "gold.html",
        "Gold",
        "Range queries, DSU, hashing, modular arithmetic, Euler tour, DP, LIS, and a trie.",
        "4_Gold",
        "Gold is where most of the notebook sits.",
        topic(
            "Point update, range query",
            "PURS",
            [
                ("notebook/data_structures/1d_range_query/FenwickTree.h", "FenwickTree.h", "Prefix sums with point updates."),
                ("notebook/data_structures/1d_range_query/SegmentTree.h", "SegmentTree.h", "Recursive segment tree."),
                ("notebook/data_structures/1d_range_query/IterativeSegmentTree.h", "IterativeSegmentTree.h", "Iterative segment tree."),
            ],
        )
        + topic(
            "Disjoint set union",
            "DSU",
            [
                ("notebook/graphs/dsu/DSU.h", "DSU.h", "Parent and size, with path compression."),
                ("python/graphs/dsu/DSU.py", "DSU.py", "The same structure in Python."),
                ("notebook/examples/graphs/dsu/323.cpp", "323.cpp", "A worked DSU problem."),
            ],
        )
        + topic(
            "Hashing",
            "Hashing",
            [
                ("notebook/strings/rolling_hash/rollinghash.h", "rollinghash.h", "Forward and backward rolling hash."),
                ("python/strings/rolling_hash/RollingHash.py", "RollingHash.py", "The same hash in Python."),
            ],
        )
        + topic(
            "Modular arithmetic",
            "Modular",
            [
                ("notebook/math/modular_arithmetic/ModFact.h", "ModFact.h", "Factorials and powers modulo 10^9+7."),
                ("notebook/math/modular_arithmetic/ModInv.h", "ModInv.h", "Modular inverse by binary exponentiation."),
                ("notebook/examples/modular_arithmetic/3881.cpp", "3881.cpp", "A worked modular problem."),
            ],
        )
        + topic(
            "Euler tour",
            "Tree_Euler",
            [
                ("notebook/trees/euler_tour/EulerTour.h", "EulerTour.h", "Entry and exit times on a tree."),
                ("contests/leetcode/solve/euler_tour", "euler_tour/", "Solved Euler-tour problems."),
            ],
        )
        + topic(
            "Dynamic programming",
            "Intro_DP",
            [
                ("notebook/examples/dynamic_programming/3418.cpp", "3418.cpp", "One DP writeup."),
                ("contests/usaco/dp", "usaco/dp/", "DP solutions."),
            ],
        )
        + topic(
            "DP on trees",
            "DP_Trees",
            [
                ("contests/leetcode/solve/dp_on_tree", "dp_on_tree/", "Tree DP solutions."),
            ],
        )
        + topic(
            "Longest increasing subsequence",
            "LIS",
            [
                ("contests/leetcode/solve/lis", "lis/", "LIS solutions."),
            ],
        )
        + topic(
            "Trie",
            None,
            [
                ("contests/leetcode/solve/trie", "trie/", "Trie solutions. The guide has no trie module, so it is filed here with the other gold structures."),
            ],
        ),
    )
    page(
        "plat.html",
        "Platinum",
        "Lazy and sparse segment trees, Mo, square-root blocks, binary lifting, and small-to-large merging.",
        "5_Plat",
        "Range updates, offline queries, and tree jumps.",
        topic(
            "Range update, range query",
            "RURQ",
            [
                ("notebook/data_structures/rurq/LazySegmentTree.h", "LazySegmentTree.h", "Segment tree with lazy range updates."),
            ],
        )
        + topic(
            "Sparse segment tree",
            "Sparse_Segtree",
            [
                ("notebook/data_structures/rurq/SparseSegmentTree.h", "SparseSegmentTree.h", "A segment tree that allocates only visited nodes."),
            ],
        )
        + topic(
            "Square root",
            "Sqrt",
            [
                ("notebook/data_structures/1d_range_query/Mo.h", "Mo.h", "Mo's algorithm over offline range queries."),
                ("notebook/data_structures/1d_range_query/SRD.h", "SRD.h", "Square-root decomposition."),
                ("contests/leetcode/solve/mo_algorithm", "mo_algorithm/", "A solved Mo problem."),
            ],
        )
        + topic(
            "Binary jumping",
            "Binary_Jump",
            [
                ("contests/leetcode/solve/binary_lifting", "binary_lifting/", "Binary lifting solutions."),
            ],
        )
        + topic(
            "Small to large",
            "Merging",
            [
                ("contests/leetcode/solve/small_to_large_merging", "small_to_large_merging/", "Small-to-large merging solutions."),
            ],
        ),
    )
    page(
        "advanced.html",
        "Advanced",
        "Persistent trees, strongly connected components, Eulerian paths, DSU rollback, and cache structures.",
        "6_Advanced",
        "Structures past the platinum modules, plus a few cache snippets that are not in the guide.",
        topic(
            "Persistent data structures",
            "Persistent",
            [
                ("notebook/data_structures/rurq/PersistentSegmentTree.h", "PersistentSegmentTree.h", "Persistent sparse segment tree."),
            ],
        )
        + topic(
            "Strongly connected components",
            "SCC",
            [
                ("contests/leetcode/solve/kosaraju", "kosaraju/", "Kosaraju solutions."),
            ],
        )
        + topic(
            "Eulerian tours",
            "Eulerian_Tours",
            [
                ("contests/leetcode/solve/eulerian_path", "eulerian_path/", "Eulerian-path solutions."),
            ],
        )
        + topic(
            "DSU rollback",
            "Offline_Del",
            [
                ("notebook/graphs/dsu/DSURollback.h", "DSURollback.h", "Disjoint set union that can undo unions."),
                ("contests/leetcode/solve/dsu_rollback", "dsu_rollback/", "A solved rollback problem."),
            ],
        )
        + """
<h2>Caches</h2>
<p>These are not USACO Guide modules. They live in <code>notebook/databases/</code>.</p>
<ul>
<li>{bloom}. Bloom filter.</li>
<li>{skip}. Skip list.</li>
<li>{hashf}. String hash factory.</li>
<li>{fifo}. FIFO eviction.</li>
<li>{lru}. LRU eviction.</li>
<li>{lfu}. LFU eviction.</li>
<li>{q2}. LRU-2Q eviction.</li>
</ul>
""".format(
            bloom=link("notebook/databases/data_structures/bloomfilter.h", "bloomfilter.h"),
            skip=link("notebook/databases/data_structures/skiplist.h", "skiplist.h"),
            hashf=link("notebook/databases/data_structures/utils/hash.h", "hash.h"),
            fifo=link("notebook/databases/eviction/fifo.h", "fifo.h"),
            lru=link("notebook/databases/eviction/lru.h", "lru.h"),
            lfu=link("notebook/databases/eviction/lfu.h", "lfu.h"),
            q2=link("notebook/databases/eviction/lru-2q.h", "lru-2q.h"),
        ),
    )


if __name__ == "__main__":
    main()
