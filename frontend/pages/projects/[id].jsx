import { useRouter } from "next/router";
import { DiffEditor } from "@monaco-editor/react";

import Header from "../../components/header";
import Layout from "../../components/layout";

const ProjectPage = () => {
  const router = useRouter();
  const { id } = router.query;

  return (
    <Layout>
      <Header />
      <DiffEditor
        height="calc(100vh - 1rem)"
        theme="vs-dark"
        modified={`#include <stdio.h>
        #include <stdlib.h>
        
        int main(int argc, char **argv) {
          if (argc != 2) {
            fprintf(stderr, "%s: invalid number of arguments\\n", argv[0]);
            return 1;
          }
        
          printf("  .globl main\\n");
          printf("main:\\n");
          printf("  mov $%d, %%rax\\n", atoi(argv[1]));
          printf("  ret\\n");
          return 0;
        }`}
        original={`#include <stdio.h>
        #include <stdlib.h>
        
        int main(int argc, char **argv) {
          if (argc != 2) {
            fprintf(stderr, "%s: invalid number of arguments\\n", argv[0]);
            return 1;
          }
        
          char *p = argv[1];
        
          printf("  .globl main\\n");
          printf("main:\\n");
          printf("  mov $%ld, %%rax\\n", strtol(p, &p, 10));
        
          while (*p) {
            if (*p == '+') {
              p++;
              printf("  add $%ld, %%rax\\n", strtol(p, &p, 10));
              continue;
            }
        
            if (*p == '-') {
              p++;
              printf("  sub $%ld, %%rax\\n", strtol(p, &p, 10));
              continue;
            }
        
            fprintf(stderr, "unexpected character: '%c'\\n", *p);
            return 1;
          }
        
          printf("  ret\\n");
          return 0;
        }`}
        options={
          {
            minimap: { enabled: false },
          }
        }
        language="c"
      />
    </Layout>
  );
};

export default ProjectPage;
