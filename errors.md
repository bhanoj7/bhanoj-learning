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

### Error ID: E-DSA-002
- Date: Day 38
- Area: DSA
- Topic: Sliding Window
- Problem: Longest Substring Without Repeating Characters

#### ❌ What I did wrong
- Tried to solve by partial reset / incorrect pointer movement
- Did not enforce a clear window invariant
- Forgot that right pointer must pause while duplicates are removed

#### 🧠 Root Cause
- Sliding window concept not internalized
- Thinking in terms of “steps” instead of “state invariant”

#### ✅ Correct Concept
- Maintain a window with all unique characters
- Use a set to track window content
- When duplicate appears, shrink from left until valid
- Only then expand right again

#### 🔁 Action Item
- Re-solve this problem after 3 days without looking
- Practice 2 more variable-size sliding window problems

#### 📌 Status
- [ ] Pending
- [ ] Revised
- [ ] Mastered
