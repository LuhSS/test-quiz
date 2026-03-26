import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct


### Meus 10 testes ###

def test_create_question_with_invalid_points():
    with pytest.raises(Exception):
        Question(title='q1', points= 0)

def test_id_incrementa_acada_choice():
    question = Question(title = "q1")

    c1 = question.add_choice('a')
    c2 = question.add_choice('b')

    assert c1.id == 1
    assert c2.id == 2

def test_deferencia_choice_falsa_verdadeira():
    question = Question(title = "q1")

    c1 = question.add_choice('a')
    c3 = question.add_choice('c', True)

    assert c1.is_correct == False
    assert c3.is_correct == True

def test_listagem_ids_choices():
    question = Question(title = "q1")

    question.add_choice('a')
    question.add_choice('b')
    question.add_choice('c', True)

    assert question._list_choice_ids() == [1,2,3]

def test_remover_choice():
    question = Question(title = "q1")

    question.add_choice('a')
    question.add_choice('b')
    question.remove_choice_by_id(1)
    
    assert len(question.choices) == 1

    question.remove_choice_by_id(2)

    assert len(question.choices) == 0

def test_remover_choice_id_invalido():
    question = Question(title = "q1")
    with pytest.raises(Exception, match="Invalid choice id 9"):
        question.remove_choice_by_id(9)

def test_remover_todas_choice():
    question = Question(title = "q1")

    question.add_choice('a')
    question.add_choice('b')
    question.add_choice('c')
    question.remove_all_choices()

    assert len(question.choices) == 0

def test_achar_choise_por_id():
    question = Question(title = "q1")

    question.add_choice('a')
    question.add_choice('b')

    assert question._find_choice_by_id(2).text == 'b'
    with pytest.raises(Exception, match="Invalid choice id 4"):
        question._find_choice_by_id(4)

def test_selacao_choices_corretas():
    question = Question(title="q1", max_selections=2)
    question.add_choice("a", True)
    question.add_choice("b")
    question.add_choice("c", True)
    
    result = question.correct_selected_choices([1, 2])
    assert result == [1]

def test_excessao_muitas_selecoes():
    question = Question(title="q1")
    question.add_choice("a")
    question.add_choice("b")
    
    with pytest.raises(Exception, match="Cannot select more than 1 choices"):
        question.correct_selected_choices([1, 2])
