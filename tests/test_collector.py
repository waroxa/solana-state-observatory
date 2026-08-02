import unittest

import collector


class CollectorTests(unittest.TestCase):
    def test_find_chain_is_case_insensitive(self):
        rows = [{"name": "Ethereum"}, {"name": "Solana", "tvl": 42}]
        self.assertEqual(collector.find_chain(rows, "solana")["tvl"], 42)

    def test_pct_change(self):
        self.assertEqual(collector.pct_change(125, 100), 25.0)
        self.assertEqual(collector.pct_change(75, 100), -25.0)
        self.assertIsNone(collector.pct_change(2, 0))

    def test_anomaly_respects_direction(self):
        drop = collector.anomaly("TPS", 60, 100, warning_pct=20, critical_pct=35, direction="down")
        self.assertEqual(drop["severity"], "critical")
        self.assertEqual(drop["deltaPct"], -40.0)
        self.assertIsNone(
            collector.anomaly("TPS", 140, 100, warning_pct=20, critical_pct=35, direction="down")
        )

    def test_health_score_healthy_snapshot(self):
        metrics = {
            "network": {"rpcHealth": "ok", "slotTimeSeconds": 0.42},
            "validators": {"delinquentStakePct": 0.2},
        }
        score = collector.health_score(metrics, [])
        self.assertEqual(score["score"], 100)
        self.assertEqual(score["status"], "healthy")

    def test_markdown_contains_provenance_and_outputs(self):
        snapshot = {
            "generatedAt": "2026-08-02T00:00:00Z",
            "health": {"score": 90, "status": "healthy"},
            "metrics": {
                "network": {"rpcHealth": "ok", "tps": 1000, "slotTimeSeconds": 0.4, "epochProgressPct": 50},
                "validators": {"active": 2, "delinquentStakePct": 0.1, "topByStake": []},
                "economics": {},
            },
            "anomalies": [],
            "coverage": {"successfulSources": 12, "totalSources": 12},
            "sources": [{"name": "Solana JSON-RPC", "url": "https://api.mainnet-beta.solana.com", "metrics": ["network"]}],
            "methodology": {"tps": "t", "slotTime": "s", "anomalies": "a", "healthScore": "h"},
        }
        report = collector.render_markdown(snapshot)
        self.assertIn("Solana JSON-RPC", report)
        self.assertIn("Machine-readable output", report)


if __name__ == "__main__":
    unittest.main()
