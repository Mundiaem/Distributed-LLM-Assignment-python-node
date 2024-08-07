import {Router} from "express";
import axios from "axios";

const router = Router();

const PYTHON_API_URL = 'http://127.0.0.1:5001';

router.post('/query', async (req, res) => {
    const {model, question} = req.body;
    await axios.post(`${PYTHON_API_URL}/select_model`, {model});
    const response = await axios.post(`${PYTHON_API_URL}/query`,
        {question});
    res.json(response.data);
});

router.get('/history', async (req, res) => {
    const response = await axios.get(`${PYTHON_API_URL}/history`);
    res.json(response.data);
});

export default router