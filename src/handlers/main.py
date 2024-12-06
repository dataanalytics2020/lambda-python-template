from typing import Dict, Any

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    AWS Lambda のメインハンドラー関数
    
    Args:
        event (Dict[str, Any]): Lambda イベントデータ
        context (Any): Lambda コンテキスト
    
    Returns:
        Dict[str, Any]: レスポンス
    """
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
