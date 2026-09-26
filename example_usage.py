import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AgentContextCompactionDeduplicatorClient

def main():
    client = AgentContextCompactionDeduplicatorClient()
    res = client.compact_context_window()
    print("=== Agent Context Compaction Deduplicator Output ===")
    print(f"Original: {res['original_token_count']:,} tokens -> Compacted: {res['post_compression_tokens']:,} tokens")
    print(f"Recovered: {res['tokens_recovered_count']:,} tokens (Ratio: {res['effective_compression_ratio']*100}%)")
    print(f"Budget Utilized: {res['token_budget_utilized_pct']} | Overflow Prevented: {res['context_overflow_prevented']}")
    print(f"Verdict: {res['verdict']}")

if __name__ == '__main__':
    main()
