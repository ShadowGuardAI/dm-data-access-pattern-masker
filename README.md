# dm-data-access-pattern-masker
Masks access patterns to data during masking operations. It can reorder the records before applying other masking techniques. This prevents attackers from inferring information about the data or masking algorithm through observing access timings and order. Simple to implement with random index shuffling. - Focused on Tools designed to generate or mask sensitive data with realistic-looking but meaningless values

## Install
`git clone https://github.com/ShadowGuardAI/dm-data-access-pattern-masker`

## Usage
`./dm-data-access-pattern-masker [params]`

## Parameters
- `--seed`: No description provided
- `--header`: Specify if the input CSV file has a header row. Defaults to False.

## License
Copyright (c) ShadowGuardAI
