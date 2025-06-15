'use client';

import React, { useState } from 'react';

interface CardProps {
  heading: string;
  isEditable: boolean;
  handleSubmitCode: Function;
  output: string;
}

const Card: React.FC<CardProps> = ({ heading, isEditable, handleSubmitCode, output }) => {
  const [text, setText] = useState('');

  return (
    <div className="w-full h-full p-6 border rounded-xl shadow-md bg-white flex flex-col">
      <h2 className="text-2xl font-semibold mb-4">{heading}</h2>

      <textarea
        className="w-full h-full p-3 border rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-blue-500"
        value={text || output}
        onChange={(e) => setText(e.target.value)}
        disabled={!isEditable}
      />

      {isEditable && (
        <button
          className="w-full mt-4 px-5 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition-all self-start"
          onClick={() => handleSubmitCode(text)}
        >
          Compile
        </button>
      )}
    </div>
  );
};

export default Card;
