import app from "../app";
import  request from "supertest"

//group test using describe SELECT_MODEL
describe("POST /api/select_model/", () =>{
    it('return status code 200 if model is passed',async () => {
        const  res = await request(app).post("/api/select_model").send({model: "LLM1"})
    // toEqual recursively check every field of an object array
        expect(res.statusCode).toEqual(404)

    });
})

//group test using describe for QUERY
describe("POST /api/query", () =>{
    it('return status code 200 if question and answer is passed',async () => {
        const  res = await request(app).post("/api/query").send({model: "LLM1", "question": "What is the weather today?"})
        // toEqual recursively check every field of an object array
        expect(res.statusCode).toEqual(200)

    });
})

//group test using describe for HISTORY
describe("GET /api/history", () =>{
    it('return status code 200 if question and answer is passed',async () => {
        const  res = await request(app).get("/api/history").send()
        // toEqual recursively check every field of an object array
        expect(res.statusCode).toEqual(200)

    });
})