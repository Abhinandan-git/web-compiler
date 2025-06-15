import './globals.css';

import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Online FFO Compiler',
  description: 'Compiler your ffo code using this online compiler',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body data-new-gr-c-s-check-loaded="14.1239.0" data-gr-ext-installed="">{children}</body>
    </html>
  );
}
