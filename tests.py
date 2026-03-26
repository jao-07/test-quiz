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

def test_create_question_with_invalid_points():
    with pytest.raises(Exception):
        Question(title='a', points=0)
    with pytest.raises(Exception):
        Question(title='a', points=-2)
    with pytest.raises(Exception):
        Question(title='a', points=101)
    with pytest.raises(Exception):
        Question(title='a', points=200)

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

def test_create_multiple_choices():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', True)
    assert question.choices[0].id != question.choices[1].id

def test_create_choice_with_invalid_text():
    question = Question(title='q1')
    with pytest.raises(Exception):
        question.add_choice('', False)
    with pytest.raises(Exception):
        question.add_choice('a'*101, False)
    with pytest.raises(Exception):
        question.add_choice('a'*500, False)
    

def test_remove_choice_by_id():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.remove_choice_by_id(1)
    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'b'
    assert choice.is_correct

def test_remove_choice_with_invalid_id():
    question = Question(title='q1')
    
    question.add_choice('a')
    with pytest.raises(Exception):
        question.remove_choice_by_id(2)
    

def test_remove_all_choices():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.remove_all_choices()
    assert len(question.choices) == 0

def test_set_correct_choices():
    question = Question(title='q1')
    question.add_choice('a')
    question.add_choice('b')
    question.add_choice('c')
    question.add_choice('d')
    question.set_correct_choices([1,3])
    assert question.choices[0].is_correct
    assert not question.choices[1].is_correct
    assert question.choices[2].is_correct
    assert not question.choices[3].is_correct

def test_set_choices_with_invalid_id():
    question = Question(title='q1')
    question.add_choice('a')
    question.add_choice('b')
    with pytest.raises(Exception):
        question.set_correct_choices([1,3])

def test_correct_selected_choices():
    question = Question(title='q1', max_selections=4)
    question.add_choice('a')
    question.add_choice('b')
    question.add_choice('c')
    question.add_choice('d')
    question.set_correct_choices([1,3])
    correct_choices = question.correct_selected_choices([1,2])
    assert correct_choices == [1]

def test_invalid_number_of_selected_choices():
    question = Question(title='q1', max_selections=1)
    question.add_choice('a')
    question.add_choice('b')
    question.add_choice('c')
    question.add_choice('d')
    question.set_correct_choices([3])
    with pytest.raises(Exception):
        correct_choices = question.correct_selected_choices([1,2])