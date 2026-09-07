class StockSpanner:
    # span: max number of consective days where stock price was less than or equal to the price that day 
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        while self.stack:
            p, sp = self.stack[-1]
            if p <= price: 
                self.stack.pop()
                span += sp
            else: 
                self.stack.append((price, span))
                return span
        
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)