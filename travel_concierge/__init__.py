# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import google.auth
from google.auth import exceptions as google_auth_exceptions


def _env_truthy(name: str, default: str = "True") -> bool:
    value = os.getenv(name, default)
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


if _env_truthy("GOOGLE_GENAI_USE_VERTEXAI", "True"):
    try:
        _, project_id = google.auth.default()
    except google_auth_exceptions.DefaultCredentialsError as err:
        raise google_auth_exceptions.DefaultCredentialsError(
            "GOOGLE_GENAI_USE_VERTEXAI is enabled but Application Default Credentials "
            "were not found. Either run `gcloud auth application-default login` or "
            "set GOOGLE_GENAI_USE_VERTEXAI=0 to use API key auth."
        ) from err
    os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
    os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
    os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")

from . import agent as agent  # noqa: E402

__all__ = ["agent"]
