import * as footers from "./footers";
import * as navbars from "./headers";

export function Base({ children }: any) {
  return (
    <div className="flex flex-col min-h-screen bg-gray-100">
      <navbars.Header />
      <main className="flex-1">{children}</main>
      <footers.Footer />
    </div>
  );
}