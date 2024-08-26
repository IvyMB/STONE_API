from flask import Blueprint, request, jsonify
from services import SaleService

best_items_bp = Blueprint('best_items_bp', __name__)


@best_items_bp.route('/best_items_by_document_id', methods=['POST'])
def get_items_by_document_id():
    data = request.json
    if not data:
        return jsonify({'message': 'Request body is required'}), 400

    # Obter o estado do corpo da solicitação
    document_id = data.get('document_id')
    if not document_id:
        return jsonify({'message': 'Document ID is required'}), 400
    
    try:
        top_sold_items = SaleService.get_best_product_by_doc_id(document_id=document_id)
        return jsonify({"result": top_sold_items}), 200
    except Exception as e:
        return jsonify({'message': f'Error fetching data: {str(e)}'}), 500


