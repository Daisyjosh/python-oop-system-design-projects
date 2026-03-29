class Auction:
    def __init__(self,auc_id,product_id,status,created_at,auction_winner=None,winning_bid = None):
        self.auc_id = auc_id
        self.product_id = product_id
        self.status = status
        self.created_at = created_at
        self.auction_winner = auction_winner
        self.winning_bid = winning_bid

