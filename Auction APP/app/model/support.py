class SupportRequest:
    def __init__(self,sr_id,user_id,issue_type,issue,description,priority,created_at):
        self.sr_id = sr_id
        self.user_id = user_id
        self.issue_type = issue_type
        self.issue = issue
        self.description = description
        self.priority = priority
        self.created_at = created_at