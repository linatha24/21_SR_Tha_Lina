# Reflection (Assignment Step 8)

### 1. What Worked Well
Running the test queries demonstrated that the local pipeline handles
factual IT support requests very well. For questions like setting up
company email or configuring VPN access, the retriever found the exact
documentation with high confidence (distances as low as 0.1914 for mobile
email setup and 0.3018 for VPN). The generation model (`qwen3:8b`)
synthesized clear, numbered steps while correctly attributing sources like
`001_Setting_Up_a_Mobile_Device_for_Company_Email.txt`. Most impressively,
the grounding prompt prevented hallucinations: when I tested the out-of-scope
question about the CEO's home address, retrieval distances jumped above
0.95–1.03, and the model correctly replied that it lacked sufficient
information to answer.

### 2. What Was Harder Than Expected
Inspecting the retrieved chunks revealed unexpected noise caused by fixed
top-k=4 retrieval. For example, when asking "How do I reset my forgotten
PIN?", the system retrieved three relevant chunks (dist 0.34–0.44), but the
fourth chunk was from `004_Troubleshooting_Issues_with_Microsoft_Office.txt`
(dist 0.9345). Although the model correctly ignored this unrelated chunk
when writing the answer, it showed how easily fixed chunk sizes and
arbitrary top-k retrieval can pollute the prompt with irrelevant context.

### 3. Idea for Improvement: Advanced RAG
To solve this noise issue, I would implement **Cross-Encoder Re-ranking**
(e.g., using `bge-reranker-base`). Instead of passing all top-4 bi-encoder
results directly to the LLM, the system could retrieve a wider candidate pool
of 8–10 chunks from ChromaDB and score them with a cross-encoder. A
cross-encoder evaluates deep token interactions between question and
passage, effectively filtering out weak matches like the Microsoft Office
chunk before prompt assembly and ensuring higher generation fidelity.
