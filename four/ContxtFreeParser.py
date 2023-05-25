# Generated from ContxtFree.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,39,2,0,7,0,1,0,1,0,1,0,3,0,6,8,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,0,1,0,1,0,0,0,45,
        0,5,1,0,0,0,2,3,6,0,-1,0,3,6,5,10,0,0,4,6,5,11,0,0,5,2,1,0,0,0,5,
        4,1,0,0,0,6,35,1,0,0,0,7,8,10,7,0,0,8,9,5,4,0,0,9,34,3,0,0,8,10,
        11,10,6,0,0,11,12,5,5,0,0,12,34,3,0,0,7,13,14,10,5,0,0,14,15,5,6,
        0,0,15,34,3,0,0,6,16,17,10,4,0,0,17,18,5,7,0,0,18,34,3,0,0,5,19,
        20,10,3,0,0,20,21,5,8,0,0,21,34,3,0,0,4,22,23,10,9,0,0,23,24,5,1,
        0,0,24,25,3,0,0,0,25,26,5,2,0,0,26,34,1,0,0,0,27,28,10,8,0,0,28,
        29,5,1,0,0,29,30,3,0,0,0,30,31,5,2,0,0,31,32,5,3,0,0,32,34,1,0,0,
        0,33,7,1,0,0,0,33,10,1,0,0,0,33,13,1,0,0,0,33,16,1,0,0,0,33,19,1,
        0,0,0,33,22,1,0,0,0,33,27,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,
        36,1,0,0,0,36,1,1,0,0,0,37,35,1,0,0,0,3,5,33,35
    ]

class ContxtFreeParser ( Parser ):

    grammarFileName = "ContxtFree.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'^'", "'*'", "'/'", "'>'", 
                     "'<'", "'&'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "PT", "NUMBER", "DBL" ]

    RULE_expr = 0

    ruleNames =  [ "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    PT=9
    NUMBER=10
    DBL=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ContxtFreeParser.NUMBER, 0)

        def DBL(self):
            return self.getToken(ContxtFreeParser.DBL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ContxtFreeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ContxtFreeParser.ExprContext,i)


        def getRuleIndex(self):
            return ContxtFreeParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ContxtFreeParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 3
                self.match(ContxtFreeParser.NUMBER)
                pass
            elif token in [11]:
                self.state = 4
                self.match(ContxtFreeParser.DBL)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 33
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ContxtFreeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 7
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 8
                        self.match(ContxtFreeParser.T__3)
                        self.state = 9
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = ContxtFreeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 10
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 11
                        self.match(ContxtFreeParser.T__4)
                        self.state = 12
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = ContxtFreeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 13
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 14
                        self.match(ContxtFreeParser.T__5)
                        self.state = 15
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = ContxtFreeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 16
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 17
                        self.match(ContxtFreeParser.T__6)
                        self.state = 18
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = ContxtFreeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 19
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 20
                        self.match(ContxtFreeParser.T__7)
                        self.state = 21
                        self.expr(4)
                        pass

                    elif la_ == 6:
                        localctx = ContxtFreeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 22
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 23
                        self.match(ContxtFreeParser.T__0)
                        self.state = 24
                        self.expr(0)
                        self.state = 25
                        self.match(ContxtFreeParser.T__1)
                        pass

                    elif la_ == 7:
                        localctx = ContxtFreeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 27
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 28
                        self.match(ContxtFreeParser.T__0)
                        self.state = 29
                        self.expr(0)
                        self.state = 30
                        self.match(ContxtFreeParser.T__1)
                        self.state = 31
                        self.match(ContxtFreeParser.T__2)
                        pass

             
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         




