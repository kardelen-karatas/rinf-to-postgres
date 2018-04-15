# rinf-to-postgres
python scripts for extracting data from rinf xml files and inserting them in a a database

## Requirements:
* python3
* lxml

## Usage:
### From the command line:
```bash
python extractor.py --rinf ../rinf.xml \
--postgres-host localhost \
--postgres-port 5433 \
--postgres-user postgres \
--postgres-password 12345678 \
--postgres-db rinf_extractor
```

### By using the class:
```python
from rinf import extractor

config = extractor.RINFExtractorConfig(
    'localhost',
    '5433',
    'postgres',
    '12345678',
    'rinf_extractor'
)

rinf_extractor = extractor.RINFExtractor(config)
rinf_extractor.parse_xml('gros_fichier.xml')
rinf_extractor.close()
```
