# Source - https://stackoverflow.com/a
# Posted by Hongbo Miao, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-01, License - CC BY-SA 4.0

import pandas as pd
from deltalake.writer import write_deltalake

df = pd.DataFrame({"x": [1, 2, 3]})
#write_deltalake("path/to/delta-tables/table1", df)

storage_options = {
    "AWS_ACCESS_KEY_ID": "minioadmin",
    "AWS_SECRET_ACCESS_KEY": "minioadminpassword",
    "endpoint_url": "http://localhost:9000",
    "AWS_S3_ALLOW_UNSAFE_RENAME": "true",
    "AWS_ALLOW_HTTP":"true",
    "aws_conditional_put": "etag",
}

write_deltalake(
    "s3://deltalake/tables/table1",
    df,
    mode="overwrite",
    storage_options=storage_options,
)
