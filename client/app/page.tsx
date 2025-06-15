"use client";

import Card from "./components/Card";
import { useState } from "react";

interface JSONObject {
  stage: string;
  exit_code: number;
  stdout: string;
  stderr: string;
}

const Index = () => {
  const [output, setOutput] = useState("");

  function formatText(jsonObject: JSONObject) {
    setOutput((jsonObject.stderr || jsonObject.stdout) + `-------------------------------\nExited with code ${jsonObject.exit_code}`);
  }

  async function handleSumbitCode(text: string) {
    console.log(text);
    
		try {
			const response = await fetch('http://localhost:8000/run', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({ source_code: text || "" }),
			});

			if (!response.ok) {
				throw new Error(`Response status: ${response.status}`);
			}

			const json = await response.json();
			formatText(json);
		} catch (error) {
			console.error('Error:', (error as Error).message);
		}
	}

  return (
    <div className="w-screen h-screen p-8 bg-gray-100 flex items-center justify-center">
      <div className="w-full gap-5 h-full flex">
        <Card heading="Input" isEditable={true} handleSubmitCode={handleSumbitCode} output="" />
        <Card heading="Output" isEditable={false} handleSubmitCode={() => {}} output={output} />
      </div>
    </div>
  );
};

export default Index;
