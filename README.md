# manticore-tests

This repo uses the manticore toolchain in order to run
tests on the Computable core contracts. These tests are
isolated from the core development and testing
framework in the
[goest](https://github.com/computablelabs/goest) repo
since Manticore uses an AGPL license. This repo is also
licensed as an AGPL repo since AGPL doesn't have a
linking exception.

The scripts in this repo validate various known attacks
against the protocol. In each case, the script contains
details about the attack. These scripts were initially
developed by the Trail-of-Bits team as part of their
audit efforts.

## Installation

Install the latest release of [Manticore](https://github.com/trailofbits/manticore).

## Failing tests 

A number of manticore scripts are failing right now.
Scripts 5 and 7 might have had their underlying issues
fixed so the failures should be genuine, but for the
other states this isn't so.

- 5: fails with manticore.exceptions.NoAliveStates (fixed)
- 7: fails with manticore.exceptions.NoAliveStates (fixed)
- 8: fails with manticore.exceptions.NoAliveStates
- 12: fails with manticore.exceptions.NoAliveStates
- 13: fails with manticore.exceptions.NoAliveStates
- 17: fails with manticore.exceptions.NoAliveStates
