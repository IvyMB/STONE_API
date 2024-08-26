from sales_manager import SalesManager
from sold_items_manager import SoldItemsManager

class StoreService:
    @staticmethod
    def get_best_store_by_state(state: str) -> dict:
        sales_manager = SalesManager(state)
        top3_dataset_result = sales_manager.top3_bests_mcc_by_state()
        top3_result = top3_dataset_result[['irs_description', 'combined_score']]
        
        # Renomeação das colunas
        top_3_mccs = top3_result.rename(columns={
            'irs_description': 'mcc_description',
            'combined_score': 'score'
        })

        result_dict= top_3_mccs.to_dict(orient='records')
        return result_dict


class SaleService:
    @staticmethod
    def get_best_product_by_doc_id(document_id: str):
        sold_items_manager = SoldItemsManager()
        top3_best_items = sold_items_manager.top3_best_items_to_sale(document_id=document_id)
        return top3_best_items

        