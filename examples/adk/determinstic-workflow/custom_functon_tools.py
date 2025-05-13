# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci.addons.adk import Toolkit, tool
from typing import Dict, Any


class ResearcherToolkit(Toolkit):

    @tool
    def get_trending_keywords(self, topic: str) -> Dict[str, Any]:
        """ Get the trending keywords for a given topic.

        Args:
            topic (str): The topic to get trending keywords for

        Returns:
            str: A JSON string containing the trending keywords
        """

        if topic == "ai":
            return {"keywords": ["agent", "stargate", "openai", "oracle"]}

        elif topic == "tiktok":
            return {"keywords": ["tiktok", "trump", "elon", "larry"]}

        else:
            return {"keywords": ["oracle"]}


class WriterToolkit(Toolkit):

    @tool
    def email_user(self, blog_post: str, user_email: str) -> str:
        """ Email the writer with the blog post.

        Args:
            blog_post (str): The blog post to email to the user
            user_email (str): The email address of the user to email the blog post to
        Returns:
            str: A message indicating that the email has been sent
        """

        return f"Email sent to user with blog post: {blog_post}"
