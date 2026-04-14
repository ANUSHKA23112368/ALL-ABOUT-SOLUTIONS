"""
Project #058: EVM Smart Contract Reentrancy & Integer Overflow Auditor
Domain: FinTech & Blockchain
Description: Opcode pattern scanner evaluating external calls prior to state storage updates
Date: 2026-04-14
"""

import re

class SmartContractAuditor:
    def check_reentrancy(self, solidity_code: str) -> list:
        findings = []
        lines = solidity_code.splitlines()
        for idx, line in enumerate(lines):
            if '.call{value:' in line:
                for next_line in lines[idx+1:idx+10]:
                    if re.search(r'balances\[.*\]\s*=', next_line):
                        findings.append({'line': idx+1, 'type': 'REENTRANCY_RISK', 'detail': 'State variable updated after external transfer call'})
        return findings

