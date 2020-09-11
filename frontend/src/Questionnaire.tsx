import React, { useState } from "react";
import {
  Container,
  Grid,
  Header,
  Segment,
  Form,
  Table,
  Radio,
  TableCellProps,
  Button,
} from "semantic-ui-react";
import BottomMenu from "./Menu";
import { server } from "./Constants";

/*
    -- TODO --
    - translate questionnaire questions
    - implement user id and hash in form as hidden fields
    - display result after succesful submission

*/

declare global {
  type Dictionary<T> = { [key: string]: T };
}
const map: Dictionary<number> = {};
for (let i = 0; i < 50; i++) {
  map["q" + i] = 0;
}

const Questionnaire = () => {
  const [state, setState] = useState({ questions: map });
  const handleChange = (e: any, { name, value }: TableCellProps) => {
    const prevState = state.questions;
    prevState[name] = Number(value);
    setState({ questions: prevState });
  };
  const questionTexts = [
    "I Am the life of the party.",
    "I Feel little concern for others.",
    "I Am always prepared.",
    "Get stressed out easily",
    "I Have a rich vocabulary",
    "I Don't talk a lot",
    "I Am interested in people",
    "I Leave my belongings around",
    "I Am relaxed most of the time",
    "I Have difficulty understanding abstract ideas",
    "I Feel comfortable around people",
    "I Insult people",
    "I Pay attention to details",
    "I Worry about things",
    "I Have a vivid imagination",
    "I Keep in the background",
    "I Sympathize with others' feelings",
    "I Make a mess of things",
    "I Seldom feel blue",
    "I Am not interested in abstract ideas",
    "I Start conversations",
    "I Am not interested in other people's problems",
    "I Get chores done right away",
    "I Am easily disturbed",
    "I Have excellent ideas",
    "I Have little to say",
    "I Have a soft heart",
    "I Often forget to put things back in their proper place",
    "I Get upset easily",
    "I Do not have a good imagination",
    "I Talk to a lot of different people at parties",
    "I Am not really interested in others",
    "I Like order",
    "I Change my mood a lot",
    "I Am quick to understand things",
    "I Don't like to draw attention to myself",
    "I Take time out for others",
    "I Shirk my duties",
    "I Have frequent mood swings",
    "I Use difficult words",
    "I Don't mind being the center of attention",
    "I Feel others' emotions",
    "I Follow a schedule",
    "I Get irritated easily",
    "I Spend time reflecting on things",
    "I Am quiet around strangers",
    "I Make people feel at ease",
    "I Am exacting in my work",
    "I Often feel blue",
    "I Am full of ideas",
  ];

  const question = (text: string, nr: number) => (
    <Table.Row textAlign="center">
      <Table.Cell textAlign="left">{text}</Table.Cell>
      <Table.Cell>
        <Radio
          name={"q" + nr}
          value="1"
          checked={state.questions["q" + nr] === 1}
          onChange={handleChange}
        />
      </Table.Cell>
      <Table.Cell>
        <Radio
          name={"q" + nr}
          value="2"
          checked={state.questions["q" + nr] === 2}
          onChange={handleChange}
        />
      </Table.Cell>
      <Table.Cell>
        <Radio
          name={"q" + nr}
          value="3"
          checked={state.questions["q" + nr] === 3}
          onChange={handleChange}
        />
      </Table.Cell>
      <Table.Cell>
        <Radio
          name={"q" + nr}
          value="4"
          checked={state.questions["q" + nr] === 4}
          onChange={handleChange}
        />
      </Table.Cell>
      <Table.Cell>
        <Radio
          name={"q" + nr}
          value="5"
          checked={state.questions["q" + nr] === 5}
          onChange={handleChange}
        />
      </Table.Cell>
    </Table.Row>
  );

  const renderQuestions = () => {
    const r = [];
    for (var i = 0; i < 50; i++) {
      r.push(question(questionTexts[i], i));
    }
    return r;
  };

  const handleSubmit = (e: any) => {
    e.preventDefault();
    const { questions } = state;

    const formData = new URLSearchParams();
    for (let i = 0; i < 50; i++) {
      formData.append("q" + i, questions["q" + i].toString());
    }

    fetch(server + "questionnaire", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: formData,
    })
      .then((r) => {
        if (r.ok) {
          return r;
        }
        if (r.status === 401 || r.status === 403 || r.status === 500) {
          localStorage.setItem("isLoggedIn", JSON.stringify(false));
          return Promise.reject(new Error("Unknown error occurred"));
        }
      })
      /*.then((response) => {
        setTimeout(() => {
          history.push("/dashboard");
        }, 2000);
        toast.success("Login successfull! Redirecting...");
        localStorage.setItem('isLoggedIn', JSON.stringify(true));
        localStorage.setItem("loggedInTime", JSON.stringify(Date.now()));
      })*/
      .catch((e) => {
        //toast.error(e.message);
        localStorage.setItem("isLoggedIn", JSON.stringify(false));
      });
  };

  return (
    <>
      <Segment>
        <Container>
          <Grid>
            <Grid.Row columns="equal" centered>
              <Grid.Column width={16}>
                <Header>Kişilik Anketi</Header>
                <Form onSubmit={handleSubmit}>
                  lorem ipsum dolor sit amet dasdadas
                  <Table definition>
                    <Table.Header>
                      <Table.Row textAlign="center">
                        <Table.HeaderCell width="6" className="coverUp" />
                        <Table.HeaderCell width="2">
                          Kesinlikle Katılmıyorum
                        </Table.HeaderCell>
                        <Table.HeaderCell width="2">
                          Kısmen Katılmıyorum
                        </Table.HeaderCell>
                        <Table.HeaderCell width="2">Nötr</Table.HeaderCell>
                        <Table.HeaderCell width="2">
                          Kısmen Katılıyorum
                        </Table.HeaderCell>
                        <Table.HeaderCell width="2">
                          Kesinlikle Katılıyorum
                        </Table.HeaderCell>
                      </Table.Row>
                    </Table.Header>

                    <Table.Body>{renderQuestions()}</Table.Body>
                  </Table>
                  <Button type="submit" primary floated="right" fluid>
                    Gönder
                  </Button>
                </Form>
              </Grid.Column>
            </Grid.Row>
          </Grid>
        </Container>
      </Segment>
      <BottomMenu />
    </>
  );
};

export default Questionnaire;
