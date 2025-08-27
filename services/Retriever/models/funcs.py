def get_aggregat( start , limit) -> list:
        aggregat = [
            
            { "$sort": { "CreateDate": 1 } },
            { "$skip": start},
            { "$limit": limit },
            { "$project" : { "_id" : 0 } }

        ]

        return aggregat



# --------------------------------------------------------------------------------------
def filter_by_info(data:list[dict] ,field:str , param ) -> list:
        
        data = list(filter(lambda x: x[field] == param , data))

        return data

