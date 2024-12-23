from pydantic import BaseModel

from llama_si_agent.service.request.llama_si_agent_code_review_request import LlamaSIAgentCodeReviewRequest


class LlamaSIAgentCodeReviewRequestForm(BaseModel):
    user_token: str
    project_name: str

    def to_si_agent_code_review_request(self) -> LlamaSIAgentCodeReviewRequest:
        return LlamaSIAgentCodeReviewRequest(user_token=self.user_token, project_name=self.project_name)
