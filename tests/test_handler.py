from typing import Dict, Any
import pytest
from src.handlers.main import lambda_handler

def test_lambda_handler() -> None:
    """
    lambda_handler関数のテスト
    """
    # テストイベントの準備
    event: Dict[str, Any] = {}
    context: Any = None
    
    # 関数の実行
    response = lambda_handler(event, context)
    
    # アサーション
    assert response['statusCode'] == 200
    assert 'body' in response
