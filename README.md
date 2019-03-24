Simplebit
---


Simplebit is a small crypto api that returns metadata on the top 500 cryptos.


---

Root Endpoint: `/`


Asset List: `/assets`
Returns 40 thin results
  - `q`: Search text


Asset Detail: `/assets/{hash}/`
Returns all information for the given asset.
  - `hash`: The asset hash


Asset Detail Field: `/assets/{hash}/{field_name}`
Returns the field for the given asset.
  - `hash`: The asset hash
  - `field_name`: A column in the asset table.
