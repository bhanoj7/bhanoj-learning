# 🧠 Personal Error Ledger

## Error ID: E-DSA-002
- Date: Dec 21
- Day: 36
- Area: DSA
- Topic: Binary Search
- Problem: Find Peak Element (LC 162)

### ❌ What I did wrong
- Initially used linear scan instead of binary search
- Ignored O(log n) requirement
- Unsafe pointer movement caused boundary risk

### 🧠 Root Cause
- Binary search invariant not internalized
- Thinking in index-scan mode instead of decision-space mode

### ✅ Correct Concept
- Peak existence is guaranteed
- Compare nums[mid] vs nums[mid+1]
- Decide slope and discard half the space

### 🔁 Action Item
- Practice 2 more binary-search-on-answer problems
- Re-explain invariant aloud without code

### 📌 Status
- [x] Corrected
- [ ] Mastered
