import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
} from "./ui/select";
import { GeneratedCodeConfig } from "../types";

function generateDisplayComponent(config: GeneratedCodeConfig) {
  switch (config) {
    case GeneratedCodeConfig.TAILWIND_DAISYUI:
      return (
        <div>
          <span className="font-semibold">Tailwind</span> +{" "}
          <span className="font-semibold">daisyUI</span>
        </div>
      );
    default:
      // TODO: Should never reach this out. Error out
      return config;
  }
}

interface Props {
  generatedCodeConfig: GeneratedCodeConfig;
  setGeneratedCodeConfig: (config: GeneratedCodeConfig) => void;
  shouldDisableUpdates?: boolean;
}

function OutputSettingsSection({
  generatedCodeConfig,
  setGeneratedCodeConfig,
  shouldDisableUpdates = false,
}: Props) {
  return (
    <div className="flex flex-col gap-y-2 justify-between text-sm">
      <div className="grid grid-cols-3 items-center gap-4">
        <span>Generating:</span>
        <Select
          value={generatedCodeConfig}
          onValueChange={(value: string) =>
            setGeneratedCodeConfig(value as GeneratedCodeConfig)
          }
          disabled={shouldDisableUpdates}
        >
          <SelectTrigger className="col-span-2" id="output-settings-js">
            {generateDisplayComponent(generatedCodeConfig)}
          </SelectTrigger>
          <SelectContent>
            <SelectGroup>
              <SelectItem value={GeneratedCodeConfig.TAILWIND_DAISYUI}>
                {generateDisplayComponent(GeneratedCodeConfig.TAILWIND_DAISYUI)}
              </SelectItem>
            </SelectGroup>
          </SelectContent>
        </Select>
      </div>
    </div>
  );
}

export default OutputSettingsSection;
