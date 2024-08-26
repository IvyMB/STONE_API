from flask import Blueprint, request, jsonify
from services import StoreService, SaleService

best_mcc_bp = Blueprint('best_mccbp', __name__)


@best_mcc_bp.route('/best_mcc_per_state', methods=['POST'])
def get_best_mcc_per_state():
    data = request.json
    if not data:
        return jsonify({'message': 'Request body is required'}), 400

    # Obter o estado do corpo da solicitação
    state = data.get('state')
    if not state:
        return jsonify({'message': 'State is required'}), 400
    
    try:
        top_mccs_df = StoreService.get_best_store_by_state(state)
        return jsonify({"result": top_mccs_df}), 200
    except Exception as e:
        return jsonify({'message': f'Error fetching data: {str(e)}'}), 500


