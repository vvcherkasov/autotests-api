from enum import Enum

class AllureStory(str,  Enum):
    LOGIN = "login"
    GET_ENTITY = "get entity"
    GET_ENTITIES = "get entities"
    CREATE_ENTITY = "create entity"
    UPDATE_ENTITY = "update entity"
    DELETE_ENTITY = "delete entity"
    VALIDATE_ENTITY = "validate entity"